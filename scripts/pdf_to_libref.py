#!/usr/bin/env python3
"""Split a Rexroth ctrlX manual (PDF) into Markdown files, one per chapter or per section, plus an
INDEX.md listing each file's entries and the PLC functions/FBs it documents.

Usage:
    pdf_to_libref.py <book.pdf> -o <out_dir> [--chapters 4-7] [--split-level 2] [--title "..."]

    PLC Libraries reference book:  pdf_to_libref.py <libs.pdf> -o references/libs
    Motion App manual:             pdf_to_libref.py <motion.pdf> -o references/motion --chapters 4-7 \
                                       --split-level 2 --title "ctrlX Motion App"

Needs poppler's `pdftotext` and `mutool` (mupdf-tools). Rerun on a new edition of the book.
"""
import argparse
import collections
import re
import shutil
import subprocess
from pathlib import Path

# Chapters that aren't libraries
SKIP = re.compile(r"^(Table of contents|About this documentation|Important directions|Safety instructions|"
                  r"Related documentation|Service and support|Index)", re.I)
HEADING_RE = re.compile(r"^\s*(\d+(?:\.\d+)+)\s+(\S.*?)\s*$")  # only used for numbers found in the PDF outline


def outline(pdf):
    """Return [(level, number, title, page)] from the PDF bookmarks."""
    out = subprocess.run(["mutool", "show", pdf, "outline"], capture_output=True, text=True, check=True).stdout
    items = []
    for line in out.splitlines():
        m = re.match(r'^[+|-]?(\t+)"(.*)"\t#page=(\d+)', line)
        if not m:
            continue
        title = m.group(2).replace("‎", "").replace('\\"', '"').strip()
        num, _, rest = title.partition(" ")
        if not re.fullmatch(r"\d+(\.\d+)*", num):
            num, rest = "", title
        items.append((len(m.group(1)), num, rest.strip(), int(m.group(3))))
    return items


def page_text(pdf, first, last):
    txt = subprocess.run(["pdftotext", "-layout", "-f", str(first), "-l", str(last), pdf, "-"],
                         capture_output=True, text=True, check=True).stdout
    return txt.split("\f")


def page_count(pdf):
    out = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout
    m = re.search(r"^Pages:\s+(\d+)", out, re.M)
    return int(m.group(1)) if m else 0


def clean_page(page, known_headings, total, figs=None):
    lines = page.splitlines()
    # Drop running header (page no + book title, then the section name) and footer
    keep = []
    for i, ln in enumerate(lines):
        s = ln.strip()
        if re.search(rf"\b\d+\s*/\s*{total}\b", s):   # running header "123 / 1344 <book title>"
            continue
        if "Bosch Rexroth AG" in s and "Edition" in s:
            continue
        if re.match(r"^Fig\. \d+:", s):
            # A caption that is just an identifier names a documented FB/function (e.g. "Fig. 243: ML_AxsPosAbs")
            m = re.match(r"^Fig\. \d+:\s+([A-Za-z]+_\w+)$", s)
            if m and figs is not None:
                figs.append(m.group(1))
            continue
        keep.append(ln.rstrip())
    # The line right after the page header is the running section title: drop first non-blank if it
    # isn't a numbered heading and is heavily indented (it sits on the right-hand side).
    for i, ln in enumerate(keep):
        if ln.strip():
            if not HEADING_RE.match(ln) and len(ln) - len(ln.lstrip()) >= 8:
                keep[i] = ""
            break
    # Side tab: lone chapter/library name in the right margin (col ~100+); table text stops near col 80
    keep = [ln for ln in keep if not (len(ln) - len(ln.lstrip()) > 90 and " " not in ln.strip())]

    # Dedent the body column, keep tables (near-zero indent) as they are
    indents = collections.Counter(len(l) - len(l.lstrip()) for l in keep if l.strip() and len(l) - len(l.lstrip()) >= 15)
    body = min((i for i, c in indents.items() if c >= max(indents.values()) * 0.3), default=0) if indents else 0
    out = []
    in_table = False
    for ln in keep:
        ind = len(ln) - len(ln.lstrip())
        # Tables ("Table N: ...") are laid out in columns from the left margin; keep them verbatim
        if (re.match(r"^Table \d+:", ln.strip()) and ind < 15) or re.match(r"^\s{0,4}Name\s+Data type\b", ln):
            in_table = True
        elif not ln.strip():
            in_table = False
        if in_table:
            out.append(ln)
            continue
        m = HEADING_RE.match(ln)
        # Must be a known section number *and* start like its outline title (wrapped cross-references
        # such as "7.5.6 KinAxsDynLimP - ... on page 660" would otherwise become headings)
        if m and m.group(1) in known_headings and \
                norm(m.group(2)).startswith(norm(known_headings[m.group(1)])[:12]) and \
                not re.search(r"on page \d+", m.group(2)):
            level = m.group(1).count(".") + 1
            out.append("")
            out.append("#" * min(level, 6) + f" {m.group(1)} {m.group(2)}")
            out.append("")
            continue
        if body and ind >= body:
            out.append(ln[body:])
        elif 5 <= ind < body:
            out.append(ln.strip())
        else:
            out.append(ln)
    return out


def norm(t):
    return re.sub(r"[^a-z0-9]", "", t.lower())


def squeeze(lines):
    res, blank = [], 0
    for ln in lines:
        if ln.strip():
            blank = 0
            res.append(ln)
        else:
            blank += 1
            if blank == 1:
                res.append("")
    return "\n".join(res).strip() + "\n"


def parse_range(spec):
    nums = set()
    for part in spec.split(","):
        lo, _, hi = part.partition("-")
        nums.update(range(int(lo), int(hi or lo) + 1))
    return nums


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("-o", "--out", required=True)
    ap.add_argument("--chapters", help="top-level chapter numbers to include, e.g. 4-7 (default: all)")
    ap.add_argument("--split-level", type=int, default=1, help="1 = file per chapter, 2 = file per section")
    ap.add_argument("--title", default="ctrlX PLC library reference")
    a = ap.parse_args()
    for tool in ("pdftotext", "mutool", "pdfinfo"):
        if not shutil.which(tool):
            raise SystemExit(f"{tool} not found")

    items = outline(a.pdf)
    total = page_count(a.pdf)
    known = {num: title for _, num, title, _ in items if "." in num}
    wanted = parse_range(a.chapters) if a.chapters else None

    def included(num):
        return num and (wanted is None or int(num.split(".")[0]) in wanted)

    # Units = items at the split level (or a shallower item with no children at that level)
    units = []
    for i, (lvl, num, title, page) in enumerate(items):
        if lvl > a.split_level or not included(num) or (lvl == 1 and SKIP.match(title)):
            continue
        has_children = i + 1 < len(items) and items[i + 1][0] > lvl
        if lvl == a.split_level or not has_children:
            units.append(i)

    out_dir = Path(a.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    index = [f"# {a.title} — index", "",
             f"Generated from `{Path(a.pdf).name}` by `scripts/pdf_to_libref.py`. "
             "Search this index (or grep the files) for a name, then read just that section.", ""]

    for idx in units:
        lvl, num, title, page = items[idx]
        nxt = next((j for j in range(idx + 1, len(items)) if items[j][0] <= lvl), None)
        nxt_num = items[nxt][1] if nxt is not None else None
        end_page = items[nxt][3] if nxt is not None else total
        pages = page_text(a.pdf, page, max(page, end_page))
        body, figs = [], []
        started = False
        for p in pages:
            for ln in clean_page(p, {**known, num: title}, total, figs if started is not False else None):
                # Trim content before this unit's heading and after the next one's
                if not started:
                    if re.match(rf"^#+ {re.escape(num)}\b", ln) or re.match(rf"^\s*{re.escape(num)}\s{{2,}}", ln):
                        started = True
                        body.append(f"# {num} {title}")
                    continue
                if nxt_num and (re.match(rf"^#+ {re.escape(nxt_num)} ", ln) or
                                re.match(rf"^\s*{re.escape(nxt_num)}\s{{2,}}\S", ln)):
                    started = None
                    break
                body.append(ln)
            if started is None:
                break
        if started is False:  # heading not found in text; keep everything
            body = [f"# {num} {title}"] + [l for p in pages for l in clean_page(p, known, total, figs)]
        fname = "-".join(f"{int(x):02d}" for x in num.split(".")) + \
            f"_{re.sub(r'[^A-Za-z0-9_]+', '_', title).strip('_')}.md"
        text = squeeze(body)
        (out_dir / fname).write_text(text, encoding="utf-8")

        # Index entry: leaf sections (skip generic "Introduction and overview" etc.) + documented PLC names
        subs = []
        j = idx + 1
        while j < len(items) and items[j][0] > lvl:
            l2, n2, t2, _ = items[j]
            is_leaf = not (j + 1 < len(items) and items[j + 1][0] > l2)
            if is_leaf and not re.match(r"(Introduction|Overview|Important|Error codes|Time response|Creating)", t2, re.I):
                subs.append(t2)
            j += 1
        kb = max(1, round(len(text.encode()) / 1024))
        index.append(f"## {num} {title}  →  `{fname}` ({kb} KB, p. {page}–{end_page})")
        index.append("")
        index.append(", ".join(subs) if subs else
                     "_Not documented in this book: open the FB's Documentation tab in the ctrlX PLC Engineering Library Manager._"
                     if len(text) < 2000 else "_(single section)_")
        plc = sorted(set(f for f in figs if not any(f == s_ for s_ in subs)))
        if plc and any(f.startswith("ML_") for f in plc):
            index.append("")
            index.append("PLC: " + ", ".join(f"`{f}`" for f in plc))
        index.append("")
        print(f"{fname:60s} {kb:5d} KB  {len(subs)} entries  {len(plc)} figs")

    (out_dir / "INDEX.md").write_text("\n".join(index), encoding="utf-8")
    print(f"Wrote {out_dir / 'INDEX.md'}")


if __name__ == "__main__":
    main()
