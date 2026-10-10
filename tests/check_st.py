"""Assertions on the PLCopenXML built from tests/fixtures (run by tests/run.sh)."""
import sys
import xml.etree.ElementTree as ET

P = "{http://www.plcopen.org/xml/tc6_0200}"
root = ET.parse(sys.argv[1]).getroot()
fails = []


def check(name, cond, detail=""):
    print(("PASS " if cond else "FAIL ") + name + ("" if cond else f"  [{detail}]"))
    if not cond:
        fails.append(name)


def tag(e):
    return e.tag.split("}")[1]


dts = {d.get("name"): d for d in root.iter(f"{P}dataType")}
check("enum, structs present", {"E_TestState", "ST_Pair", "ST_Nested"} <= set(dts), list(dts))
vals = [(v.get("name"), v.get("value")) for v in dts["E_TestState"].iter(f"{P}value")]
check("enum values continue after an explicit one", vals == [("Idle", "0"), ("Running", "1"), ("Done", "5"), ("Faulted", "6")], vals)
check("enum keeps base type UINT", dts["E_TestState"].find(f".//{P}enum/{P}baseType/{P}UINT") is not None)
members = [v.get("name") for v in dts["ST_Nested"].iter(f"{P}variable")]
check("struct members in order", members == ["stPair", "aiVals", "sName"], members)
check("struct member with initial value", dts["ST_Pair"].find(f".//{P}variable[@name='rB']/{P}initialValue") is not None)
check("array member type", dts["ST_Nested"].find(f".//{P}variable[@name='aiVals']/{P}type/{P}array") is not None)
check("STRING(15) member", dts["ST_Nested"].find(f".//{P}variable[@name='sName']/{P}type/{P}string") is not None)

gv = {g.get("name"): g for g in root.iter(f"{P}globalVars")}
check("GVLs named after their files", {"GVL_Test", "GVL_Const", "GVL_Retain"} <= set(gv), list(gv))
check("GVL CONSTANT flagged", gv["GVL_Const"].get("constant") == "true")
check("GVL PERSISTENT RETAIN flagged", gv["GVL_Retain"].get("retain") == "true" and gv["GVL_Retain"].get("persistent") == "true")
check("GVL simple initial value", gv["GVL_Test"].find(f"{P}variable[@name='iCount']/{P}initialValue/{P}simpleValue").get("value") == "3")

pous = {p.get("name"): p for p in root.iter(f"{P}pou")}
check("POU kinds", {n: p.get("pouType") for n, p in pous.items() if n in ("FB_All", "Fn_Add", "PRG_Test")}
      == {"FB_All": "functionBlock", "Fn_Add": "function", "PRG_Test": "program"})
blocks = [(tag(c), c.get("constant")) for c in pous["FB_All"].find(f"{P}interface") if tag(c) != "documentation"]
check("FB var blocks in house order incl. IN_OUT CONSTANT / VAR CONSTANT", blocks ==
      [("inputVars", None), ("outputVars", None), ("inOutVars", None), ("inOutVars", "true"),
       ("localVars", None), ("localVars", "true")], blocks)
check("function return type", pous["Fn_Add"].find(f"{P}interface/{P}returnType/{P}REAL") is not None)
body = "".join(pous["FB_All"].find(f"{P}body/{P}ST").itertext())
check("ST body kept, no END_FUNCTION_BLOCK", "CASE _eState OF" in body and "END_CASE" in body and "END_FUNCTION_BLOCK" not in body)
check("FB instance typed as derived TON", pous["FB_All"].find(f".//{P}variable[@name='_fbTimer']/{P}type/{P}derived").get("name") == "TON")
check("broken file produced no POU", "FB_Broken" not in pous)
sys.exit(1 if fails else 0)
