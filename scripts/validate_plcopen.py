#!/usr/bin/env python3
"""Validate PLCopenXML files against the PLCopen TC6 v2.01 schema.

Usage:
    validate_plcopen.py Project.xml [more.xml ...] [--xsd tc6_xml_v201.xsd]

CODESYS and ctrlX PLC Engineering write the tc6_0200 namespace, while the published schema
is tc6_0201. The structure is the same, so the namespace is swapped before validating. Real
editor exports pass this check, so a failure means the file is malformed, not just vendor-
flavoured. Passing doesn't prove the editor will import it the way you meant (see the
codesys-lad skill's ld_trace.py for ladder).

The schema is downloaded once into ~/.cache/plcopen/ unless --xsd points at a copy.
Needs lxml (pip install lxml).
"""
import argparse
import sys
import urllib.request
from pathlib import Path

XSD_URL = "https://raw.githubusercontent.com/beremiz/beremiz/master/plcopen/tc6_xml_v201.xsd"
CACHE = Path.home() / ".cache" / "plcopen" / "tc6_xml_v201.xsd"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="+")
    ap.add_argument("--xsd", type=Path, default=None, help="local copy of tc6_xml_v201.xsd")
    a = ap.parse_args()
    try:
        from lxml import etree
    except ImportError:
        sys.exit("ERROR: needs lxml (pip install lxml)")
    xsd = a.xsd or CACHE
    if not xsd.exists():
        print(f"Downloading the PLCopen schema to {xsd}", file=sys.stderr)
        xsd.parent.mkdir(parents=True, exist_ok=True)
        urllib.request.urlretrieve(XSD_URL, xsd)
    schema = etree.XMLSchema(etree.parse(str(xsd)))
    bad = 0
    for f in a.files:
        raw = Path(f).read_bytes().lstrip(b"\xef\xbb\xbf").replace(b"tc6_0200", b"tc6_0201")
        if schema.validate(etree.fromstring(raw)):
            print(f"VALID    {f}")
        else:
            bad += 1
            print(f"INVALID  {f}")
            for err in list(schema.error_log)[:10]:
                print(f"    line {err.line}: {err.message}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
