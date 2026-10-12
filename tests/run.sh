#!/usr/bin/env bash
# Regression test for the ctrlx-engineer scripts:
#  1. st_to_plcopenxml.py on fixtures covering every construct it converts (DUTs, GVL kinds, FB/FUNCTION/
#     PROGRAM, all var blocks), checked structurally (check_st.py), against the PLCopen schema, and for
#     the expected warnings;
#  2. the shipped example references/examples/FB_AxisCtrl.st builds and validates;
#  3. plceng.py (PLC Engineering API client) against the mock tests/mock_plceng.py;
#  4. pdf_to_libref.py regenerates references/libs and references/motion byte-identical from docs/*.pdf
#     (skipped if the PDFs or pdftotext are missing).
# The ladder side is tested by ../codesys-lad/tests/run.sh. Exits non-zero on any failure.
set -euo pipefail
ST="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$(mktemp -d)"
trap 'rm -rf "$OUT"' EXIT
cd "$ST/tests/fixtures"

echo "== converter: fixtures"
python3 "$ST/scripts/st_to_plcopenxml.py" Types.st GVL_Test.st GVL_Const.st GVL_Retain.st POUs.st Broken.st \
    -o "$OUT/fixtures.xml" 2> "$OUT/warn.txt"
python3 "$ST/scripts/validate_plcopen.py" "$OUT/fixtures.xml"
python3 "$ST/tests/check_st.py" "$OUT/fixtures.xml"
for w in "kept only in the plain-text declaration" "GVL_Test.stPair: structured initial value kept as raw text" \
         "Broken.st: no recognised objects"; do
    grep -q "$w" "$OUT/warn.txt" && echo "PASS warning: $w" || { echo "FAIL missing warning: $w"; cat "$OUT/warn.txt"; exit 1; }
done

echo "== converter: shipped example FB_AxisCtrl"
python3 "$ST/scripts/st_to_plcopenxml.py" ST_Dynamics.st "$ST/references/examples/FB_AxisCtrl.st" -o "$OUT/axis.xml" 2>/dev/null
python3 "$ST/scripts/validate_plcopen.py" "$OUT/axis.xml"

echo "== plceng.py: PLC Engineering API client against the mock"
python3 "$ST/tests/test_plceng.py"

echo "== pdf_to_libref: references regenerate identically"
LIBS_PDF="$ST/docs/R911430583_01_EN_ctrlX PLC Engineering, PLC Libraries 03VRS, Reference Book.pdf"
MOTION_PDF="$ST/docs/R911430551_01_EN_Motion App Version 4_ApplicationManual.pdf"
if command -v pdftotext >/dev/null && command -v mutool >/dev/null && [ -f "$LIBS_PDF" ] && [ -f "$MOTION_PDF" ]; then
    python3 "$ST/scripts/pdf_to_libref.py" "$LIBS_PDF" -o "$OUT/libs" > /dev/null
    python3 "$ST/scripts/pdf_to_libref.py" "$MOTION_PDF" -o "$OUT/motion" --chapters 4-7 --split-level 2 \
        --title "ctrlX Motion App" > /dev/null
    diff -rq "$OUT/libs" "$ST/references/libs" && echo "PASS references/libs identical" \
        || { echo "FAIL references/libs differ from a fresh conversion"; exit 1; }
    diff -rq "$OUT/motion" "$ST/references/motion" && echo "PASS references/motion identical" \
        || { echo "FAIL references/motion differ from a fresh conversion"; exit 1; }
else
    echo "SKIP (pdftotext/mutool or docs/*.pdf missing)"
fi
echo "ALL OK"
