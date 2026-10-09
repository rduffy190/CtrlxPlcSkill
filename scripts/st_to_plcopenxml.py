#!/usr/bin/env python3
"""Convert Structured Text source files into a CODESYS-importable PLCopenXML file.

Usage:
    st_to_plcopenxml.py file1.st [file2.st ...] -o Project.xml [--name ProjectName]

Supported top-level objects (one or more per file):
    PROGRAM / FUNCTION_BLOCK / FUNCTION ... END_PROGRAM / END_FUNCTION_BLOCK / END_FUNCTION
    TYPE ... END_TYPE            (STRUCT and enum DUTs; aliases emitted as derived types)
    VAR_GLOBAL ... END_VAR       (a GVL, named after the file stem)

Not converted (warned about): METHOD, PROPERTY, ACTION, INTERFACE, UNION, attributes on DUTs.
Each POU also carries its declaration as plain text (CODESYS addData), which preserves
comments and pragmas on import.
"""
import argparse
import datetime as dt
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

NS = "http://www.plcopen.org/xml/tc6_0200"
XHTML = "http://www.w3.org/1999/xhtml"
ET.register_namespace("", NS)

ELEMENTARY = {
    "BOOL", "BYTE", "WORD", "DWORD", "LWORD", "SINT", "INT", "DINT", "LINT",
    "USINT", "UINT", "UDINT", "ULINT", "REAL", "LREAL", "TIME", "DATE", "DT", "TOD",
    "STRING", "WSTRING",
}
ALIASES = {"TIME_OF_DAY": "TOD", "DATE_AND_TIME": "DT"}

VAR_KINDS = {
    "VAR_INPUT": "inputVars", "VAR_OUTPUT": "outputVars", "VAR_IN_OUT": "inOutVars",
    "VAR": "localVars", "VAR_TEMP": "tempVars", "VAR_EXTERNAL": "externalVars",
    "VAR_GLOBAL": "globalVars", "VAR_STAT": "localVars", "VAR_INST": "localVars",
}

warnings: list[str] = []


def q(tag):
    return f"{{{NS}}}{tag}"


def sub(parent, tag, **attrs):
    return ET.SubElement(parent, q(tag), {k: str(v) for k, v in attrs.items()})


def xhtml(parent, text):
    el = ET.SubElement(parent, f"{{{XHTML}}}xhtml")
    el.text = text
    return el


# ---------------------------------------------------------------- comments

def strip_comments(src: str) -> str:
    """Remove (* *) and // comments, keeping string literals intact."""
    out, i, n = [], 0, len(src)
    while i < n:
        c = src[i]
        if c in "'\"":
            j = src.find(c, i + 1)
            j = n if j < 0 else j + 1
            out.append(src[i:j]); i = j
        elif src.startswith("(*", i):
            j = src.find("*)", i + 2)
            i = n if j < 0 else j + 2
            out.append(" ")
        elif src.startswith("//", i):
            j = src.find("\n", i)
            i = n if j < 0 else j
        else:
            out.append(c); i += 1
    return "".join(out)


# ---------------------------------------------------------------- types

def type_element(parent, tstr: str, where: str):
    t = tstr.strip()
    tu = t.upper()
    tu = ALIASES.get(tu, tu)
    m = re.fullmatch(r"(W?STRING)\s*[\(\[]\s*(\d+)\s*[\)\]]", t, re.I)
    if m:
        sub(parent, m.group(1).lower(), length=m.group(2))
        return
    if tu in ELEMENTARY:
        sub(parent, tu if tu not in ("STRING", "WSTRING") else tu.lower())
        return
    m = re.fullmatch(r"ARRAY\s*\[(.+?)\]\s*OF\s+(.+)", t, re.I | re.S)
    if m and "*" in m.group(1):
        # Variable-length array (VAR_IN_OUT ARRAY[*]): no numeric bounds in PLCopen, so name it;
        # the plain-text declaration carries the exact type
        warnings.append(f"{where}: variable-length '{t}' emitted as derived type; "
                        "the plain-text declaration has the exact type")
        sub(parent, "derived", name=" ".join(t.split()))
        return
    if m:
        arr = sub(parent, "array")
        for dim in m.group(1).split(","):
            lo, _, hi = dim.partition("..")
            sub(arr, "dimension", lower=lo.strip(), upper=hi.strip())
        type_element(sub(arr, "baseType"), m.group(2), where)
        return
    m = re.fullmatch(r"POINTER\s+TO\s+(.+)", t, re.I | re.S)
    if m:
        type_element(sub(sub(parent, "pointer"), "baseType"), m.group(1), where)
        return
    if re.match(r"REFERENCE\s+TO\b", t, re.I):
        warnings.append(f"{where}: '{t}' emitted as derived type; check after import "
                        "(the plain-text interface should preserve it)")
    sub(parent, "derived", name=t)


def parse_var_block(body: str, where: str):
    """Yield (names, type, init, comment, address) for each declaration in a VAR block."""
    # Keep trailing // comments per declaration as documentation.
    decls, buf, comment = [], "", ""
    for line in body.splitlines():
        code, _, cmt = line.partition("//")
        code = strip_comments(code)
        if code.strip().startswith("{"):   # pragma line
            continue
        buf += " " + code
        if cmt.strip():
            comment = cmt.strip()
        while ";" in buf:
            stmt, buf = buf.split(";", 1)
            if stmt.strip():
                decls.append((stmt.strip(), comment))
            comment = ""
    for stmt, comment in decls:
        if ":" not in stmt:
            warnings.append(f"{where}: could not parse declaration '{stmt}'")
            continue
        lhs, rhs = stmt.split(":", 1)
        init = None
        if ":=" in rhs:
            rhs, init = rhs.split(":=", 1)
            init = init.strip()
        # FB instance with parameter init: fbT : TON := (PT := T#1S) handled by init above
        addr = None
        m = re.search(r"\bAT\s+(%\S+)", lhs, re.I)
        if m:
            addr = m.group(1)
            lhs = lhs[: m.start()]
        names = [n.strip() for n in lhs.split(",") if n.strip()]
        yield names, " ".join(rhs.split()), init, comment, addr


def vars_into(parent, block_body: str, where: str):
    for names, tstr, init, comment, addr in parse_var_block(block_body, where):
        for name in names:
            v = sub(parent, "variable", name=name, **({"address": addr} if addr else {}))
            type_element(sub(v, "type"), tstr, f"{where}.{name}")
            if init is not None:
                iv = sub(v, "initialValue")
                if init.startswith("[") or init.startswith("("):
                    warnings.append(f"{where}.{name}: structured initial value kept as raw text")
                sub(iv, "simpleValue", value=init)
            if comment:
                xhtml(sub(v, "documentation"), comment)


VAR_BLOCK_RE = re.compile(
    r"^\s*(VAR_INPUT|VAR_OUTPUT|VAR_IN_OUT|VAR_TEMP|VAR_EXTERNAL|VAR_GLOBAL|VAR_STAT|VAR_INST|VAR)"
    r"((?:[ \t]+(?:CONSTANT|RETAIN|PERSISTENT))*)[ \t]*$(.*?)^\s*END_VAR\s*$",
    re.I | re.M | re.S,
)


def add_var_blocks(iface, decl_text: str, where: str):
    for m in VAR_BLOCK_RE.finditer(decl_text):
        kind = m.group(1).upper()
        mods = m.group(2).upper().split()
        attrs = {}
        if "CONSTANT" in mods: attrs["constant"] = "true"
        if "RETAIN" in mods: attrs["retain"] = "true"
        if "PERSISTENT" in mods: attrs["persistent"] = "true"
        blk = sub(iface, VAR_KINDS[kind], **attrs)
        vars_into(blk, m.group(3), where)


# ---------------------------------------------------------------- objects

POU_RE = re.compile(
    r"^[ \t]*((?:\{[^}]*\}\s*)*)(PROGRAM|FUNCTION_BLOCK|FUNCTION)\s+(\w+)(.*?)$(.*?)^\s*END_\2\b;?",
    re.I | re.M | re.S,
)
TYPE_RE = re.compile(r"^[ \t]*((?:\{[^}]*\}\s*)*)TYPE\b(.*?)^\s*END_TYPE\b;?", re.I | re.M | re.S)
GVL_RE = re.compile(r"^[ \t]*VAR_GLOBAL\b.*?^\s*END_VAR\b", re.I | re.M | re.S)
UNSUPPORTED_RE = re.compile(r"^\s*(METHOD|PROPERTY|ACTION|INTERFACE)\b\s*(\w*)", re.I | re.M)


def split_decl_body(rest: str):
    """Split text after the POU header into (declaration, implementation)."""
    lines = rest.splitlines(keepends=True)
    i, in_var = 0, False
    last_decl_end = 0
    for idx, line in enumerate(lines):
        s = line.strip().upper()
        if in_var:
            if re.match(r"END_VAR\b", s):
                in_var = False
                last_decl_end = idx + 1
            continue
        if re.match(r"VAR(_\w+)?\b", s):
            in_var = True
            continue
        if s == "" or s.startswith("//") or s.startswith("(*") or s.startswith("{"):
            continue
        break
    i = last_decl_end
    return "".join(lines[:i]), "".join(lines[i:])


def add_pou(pous, attrs, kind, name, header_rest, rest, src_name):
    kind_u = kind.upper()
    pou_type = {"PROGRAM": "program", "FUNCTION_BLOCK": "functionBlock",
                "FUNCTION": "function"}[kind_u]
    pou = sub(pous, "pou", name=name, pouType=pou_type)
    iface = sub(pou, "interface")
    decl, impl = split_decl_body(rest)
    if kind_u == "FUNCTION":
        m = re.match(r"\s*:\s*([^\n;]+)", header_rest)
        if m:
            type_element(sub(iface, "returnType"), m.group(1), name)
        else:
            warnings.append(f"{name}: FUNCTION without return type")
    if re.search(r"\b(EXTENDS|IMPLEMENTS)\b", header_rest, re.I):
        warnings.append(f"{name}: EXTENDS/IMPLEMENTS kept only in plain-text interface; verify after import")
    add_var_blocks(iface, decl, name)
    plain = f"{attrs}{kind_u} {name}{header_rest}\n{decl.lstrip(chr(10))}".rstrip() + "\n"
    ad = sub(iface, "addData")
    d = sub(ad, "data", name="http://www.3s-software.com/plcopenxml/interfaceasplaintext",
            handleUnknown="implementation")
    xhtml(ET.SubElement(d, "InterfaceAsPlainText"), plain)
    body = sub(pou, "body")
    xhtml(sub(body, "ST"), impl.strip("\n") + "\n")
    if UNSUPPORTED_RE.search(impl):
        warnings.append(f"{name}: METHOD/PROPERTY/ACTION text found in body; add those objects manually")


def plaintext_adddata(parent, text):
    """CODESYS keeps the declaration as plain text (comments, pragmas, attributes) in addData."""
    ad = sub(parent, "addData")
    d = sub(ad, "data", name="http://www.3s-software.com/plcopenxml/interfaceasplaintext",
            handleUnknown="implementation")
    xhtml(ET.SubElement(d, "InterfaceAsPlainText"), text.strip("\n") + "\n")


def add_types(data_types, type_block: str, attrs: str, src_name, full_text: str = ""):
    if attrs.strip():
        warnings.append(f"{src_name}: attributes {attrs.strip()} are kept only in the plain-text "
                        "declaration; check they are present after import")
    first_new = len(data_types)
    clean = strip_comments(type_block)
    # STRUCT
    for m in re.finditer(r"(\w+)\s*(?:EXTENDS\s+\w+\s*)?:\s*STRUCT\b(.*?)END_STRUCT\s*;?", clean, re.I | re.S):
        dtp = sub(data_types, "dataType", name=m.group(1))
        st = sub(sub(dtp, "baseType"), "struct")
        vars_into(st, m.group(2), m.group(1))
        clean = clean.replace(m.group(0), "")
    # Enum: Name : ( A := 0, B, C ) [BASETYPE] ;
    for m in re.finditer(r"(\w+)\s*:\s*\((.*?)\)\s*(\w+)?\s*;", clean, re.S):
        dtp = sub(data_types, "dataType", name=m.group(1))
        en = sub(sub(dtp, "baseType"), "enum")
        values = sub(en, "values")
        nxt = 0
        for item in m.group(2).split(","):
            item = item.strip()
            if not item:
                continue
            vname, _, vval = item.partition(":=")
            if vval.strip():
                nxt = int(vval.strip(), 0)
            sub(values, "value", name=vname.strip(), value=nxt)
            nxt += 1
        if m.group(3):
            type_element(sub(en, "baseType"), m.group(3), m.group(1))
        clean = clean.replace(m.group(0), "")
    # Alias: Name : TYPE;
    for m in re.finditer(r"(\w+)\s*:\s*([^;()]+?)\s*;", clean, re.S):
        if m.group(2).strip().upper().startswith("UNION"):
            warnings.append(f"{m.group(1)}: UNION not supported")
            continue
        dtp = sub(data_types, "dataType", name=m.group(1))
        type_element(sub(dtp, "baseType"), m.group(2), m.group(1))
    if full_text:
        for dtp in list(data_types)[first_new:]:
            plaintext_adddata(dtp, full_text)


def build(files, project_name):
    now = dt.datetime.now().replace(microsecond=0).isoformat()
    root = ET.Element(q("project"))
    sub(root, "fileHeader", companyName="", productName="CODESYS",
        productVersion="CODESYS V3.5", creationDateTime=now)
    ch = sub(root, "contentHeader", name=project_name, modificationDateTime=now)
    ci = sub(ch, "coordinateInfo")
    for lang in ("fbd", "ld", "sfc"):
        sub(sub(ci, lang), "scaling", x=1, y=1)
    types = sub(root, "types")
    data_types = sub(types, "dataTypes")
    pous = sub(types, "pous")
    instances = sub(root, "instances")
    sub(instances, "configurations")
    gvls = []

    for path in files:
        src = Path(path).read_text(encoding="utf-8-sig")
        consumed = src
        for m in TYPE_RE.finditer(src):
            add_types(data_types, m.group(2), m.group(1), path, m.group(0))
            consumed = consumed.replace(m.group(0), "")
        for m in POU_RE.finditer(consumed):
            add_pou(pous, m.group(1), m.group(2), m.group(3), m.group(4), m.group(5), path)
        remaining = POU_RE.sub("", consumed)
        blocks = [m.group(0) for m in GVL_RE.finditer(remaining)]
        if blocks:
            # One GVL per file, even if it mixes VAR_GLOBAL and VAR_GLOBAL CONSTANT blocks
            text = remaining.strip()
            gvls.append((Path(path).stem, blocks, text))
        if not (TYPE_RE.search(src) or POU_RE.search(src) or GVL_RE.search(src)):
            warnings.append(f"{path}: no recognised objects (did you include END_... keywords?)")

    if gvls:
        ad = sub(root, "addData")
        for gname, blocks, text in gvls:
            d = sub(ad, "data", name="http://www.3s-software.com/plcopenxml/globalvars",
                    handleUnknown="implementation")
            gv = sub(d, "globalVars", name=gname)
            matches = [VAR_BLOCK_RE.search(b) for b in blocks]
            mods = [set((m.group(2) or "").upper().split()) if m else set() for m in matches]
            # Attributes only when every block agrees; the plain text keeps the exact blocks
            for flag in ("CONSTANT", "RETAIN", "PERSISTENT"):
                if mods and all(flag in md for md in mods):
                    gv.set(flag.lower(), "true")
            if len(blocks) > 1 and len({frozenset(md) for md in mods}) > 1:
                warnings.append(f"{gname}: mixed VAR_GLOBAL blocks (e.g. CONSTANT and normal) are exact "
                                "only in the plain-text declaration; check after import")
            for m in matches:
                vars_into(gv, m.group(3) if m else "", gname)
            plaintext_adddata(gv, text)
    return root


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="+")
    ap.add_argument("-o", "--output", required=True)
    ap.add_argument("--name", default=None, help="project name in contentHeader")
    a = ap.parse_args()
    root = build(a.files, a.name or Path(a.output).stem)
    ET.indent(root)
    xml = ET.tostring(root, encoding="unicode")
    # Match CODESYS's own exports: default-namespaced <xhtml> rather than an html: prefix
    xml = xml.replace(f' xmlns:html="{XHTML}"', "", 1)
    xml = xml.replace("<html:xhtml>", f'<xhtml xmlns="{XHTML}">').replace("</html:xhtml>", "</xhtml>")
    xml = xml.replace("<html:xhtml />", f'<xhtml xmlns="{XHTML}" />')
    Path(a.output).write_text('<?xml version="1.0" encoding="utf-8"?>\n' + xml + "\n", encoding="utf-8")
    for w in warnings:
        print("WARNING:", w, file=sys.stderr)
    print(f"Wrote {a.output}")


if __name__ == "__main__":
    main()
