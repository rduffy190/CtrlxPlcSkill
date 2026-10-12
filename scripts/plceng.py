#!/usr/bin/env python3
"""Drive ctrlX PLC Engineering (ctrlX WORKS) through its PLC Engineering REST API v2 (stdlib only).

Interface notes: references/plc-engineering-api.md. Full spec: references/plc-engineering-api-v2.json.

  plceng.py info                              product version + open project (name, path, profile)
  plceng.py tree [path] [--depth N]           element tree (default Device), "name [elementType]"
  plceng.py get <path> [--code]               one element as JSON; --code prints declaration/implementation
  plceng.py push <file.st> ... [--prune] [--dry-run]
                                              create or update DUTs/GVLs/FUNCTIONs/FBs/PROGRAMs from .st
                                              files (the same format st_to_plcopenxml.py takes);
                                              --prune also deletes POU/DUT/GVL/ITF objects not in the files
  plceng.py delete <path>                     delete an element and its children
  plceng.py task <task> <PRG> [<PRG> ...]     set the programs a task calls (replaces the list)
  plceng.py lib-find <text>                   search the System library repository
  plceng.py lib-add <name> [<version>]        add a library (newest version if omitted)
  plceng.py lib-rm <placeholder>              remove a library by its placeholder name (e.g. CXA_PLCOPEN)
  plceng.py build                             build the active application, print errors/warnings
  plceng.py save                              save the project
  plceng.py export-xml <path> <winDir> <file> export an element as PLCopenXML on the ENGINEERING PC
  plceng.py job '<json>'                      run any job ({"jobType":..., "jobParameters":{...}})

Paths are element paths below /devices, e.g. "Device/Plc Logic/Application/PRG_Main"; a leading
"/devices/" is accepted. push/delete default to the application --app (Device/Plc Logic/Application).

Connection: PLCENG_URL is REQUIRED, no default: <ip>[:port] or http://<ip>:<port> of the PC running
ctrlX PLC Engineering (port 9004 if omitted). Ask the user for that IP. If it can't be reached (the
PC's firewall often blocks 9004), the error prints a reverse SSH tunnel command to offer the user:
they run it on the engineering PC, and PLCENG_URL=localhost:9004 then works here.
"""
import getpass
import json
import os
import re
import socket
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

DEFAULT_PORT = 9004


def normalise_url(raw):
    """'10.1.10.133', '10.1.10.133:9004' or 'http://10.1.10.133:9004' -> 'http://10.1.10.133:9004'."""
    raw = raw.strip().rstrip("/")
    if not raw:
        return ""
    if "://" not in raw:
        raw = "http://" + raw
    parts = urllib.parse.urlsplit(raw)
    return f"{parts.scheme}://{parts.hostname}:{parts.port or DEFAULT_PORT}"


URL = normalise_url(os.environ.get("PLCENG_URL", ""))
API = f"{URL}/plc/engineering/api/v2"
APP = "Device/Plc Logic/Application"
BUILD_PROPS = {"build": {"excludeFromBuild": False, "external": False, "enableSystemCall": False,
                         "linkAlways": False, "compilerDefines": ""}}
CODE_TYPES = {"POU", "DUT", "GVL", "ITF"}     # what --prune may delete; folders, tasks, libraries stay


class ApiError(Exception):
    def __init__(self, status, problem):
        self.status, self.problem = status, problem
        msg = problem.get("dynamicDescription") or problem.get("detail") if isinstance(problem, dict) else problem
        super().__init__(f"HTTP {status}: {msg}")


def tunnel_hint():
    """The reverse SSH tunnel the user can open on the engineering PC when port 9004 is blocked."""
    host = urllib.parse.urlsplit(URL).hostname
    port = urllib.parse.urlsplit(URL).port or DEFAULT_PORT
    me = "<this-machine-ip>"
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((host if host not in ("localhost", "127.0.0.1") else "8.8.8.8", 9))
        me = s.getsockname()[0]
        s.close()
    except OSError:
        pass
    return (f"ssh -N -R {port}:localhost:{port} {getpass.getuser()}@{me}\n"
            f"  (run it in a normal PowerShell/cmd on the engineering PC, log in, leave the window open; "
            f"needs an SSH server on this machine; then use PLCENG_URL=localhost:{port})")


def http(method, path, body=None, timeout=60):
    if not URL:
        sys.exit("PLCENG_URL is not set: ask the user for the IP address of the PC running ctrlX PLC "
                 "Engineering, then run with PLCENG_URL=<ip>[:port] (port 9004 if omitted)")
    url = f"{API}/{urllib.parse.quote(path.lstrip('/'), safe='/')}"
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data, {"Content-Type": "application/json"}, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            raw = r.read()
            return json.loads(raw) if raw.strip() else None
    except urllib.error.HTTPError as e:
        raw = e.read()
        try:
            problem = json.loads(raw)
        except ValueError:
            problem = raw.decode(errors="replace")
        raise ApiError(e.code, problem) from None
    except (urllib.error.URLError, OSError) as e:
        local = urllib.parse.urlsplit(URL).hostname in ("localhost", "127.0.0.1")
        msg = f"cannot reach the PLC Engineering API at {URL} ({getattr(e, 'reason', e)}).\n"
        if local:
            msg += ("The reverse SSH tunnel is probably closed: ask the user to reopen it on the engineering PC:\n  "
                    + tunnel_hint())
        else:
            msg += ("Ask the user to confirm the IP and that ctrlX PLC Engineering is running with the API. "
                    "If the PC answers ping but port 9004 times out, its firewall blocks it: offer the "
                    "reverse SSH tunnel, run on the engineering PC:\n  " + tunnel_hint())
        sys.exit(msg)


def dev(path):
    """Element path -> API path below /devices."""
    path = path.strip("/")
    if path.startswith("devices/"):
        path = path[len("devices/"):]
    return f"devices/{path}"


def run_job(job, poll=1.0, timeout=600):
    """POST a job and wait for Done/Failed. Returns the final job JSON."""
    j = http("POST", "jobs", job)
    end = time.time() + timeout
    while j.get("state") not in ("Done", "Failed"):
        if time.time() > end:
            sys.exit(f"job {j.get('id')} still {j.get('state')} after {timeout}s")
        time.sleep(poll)
        j = http("GET", f"jobs/{j['id']}")
    return j


def print_job(j):
    print(j["state"])
    for part in (j.get("jobResultInfo") or "").split(" | "):
        print("  " + part)
    return 0 if j["state"] == "Done" else 1


# ----- .st parsing (same file format as st_to_plcopenxml.py) -----

START = re.compile(r"^(FUNCTION_BLOCK|FUNCTION|PROGRAM|TYPE|INTERFACE)\b\s*(\w*)")
POU_END = re.compile(r"^END_(FUNCTION_BLOCK|FUNCTION|PROGRAM)\b")


def split_st(text, stem):
    """Objects in one .st file as dicts {kind, name, lines}. A GVL_* file is one GVL (all its
    VAR_GLOBAL blocks). Comment/attribute lines directly above an object belong to it."""
    lines = text.rstrip("\n").splitlines()
    if stem.startswith("GVL_") or (lines and any(l.startswith("VAR_GLOBAL") for l in lines)
                                    and not any(START.match(l) for l in lines)):
        return [{"kind": "GVL", "name": stem, "lines": lines}]
    objs, pending, cur = [], [], None
    for ln in lines:
        if cur is None:
            m = START.match(ln)
            if m:
                cur = {"kind": m.group(1), "name": m.group(2), "lines": pending + [ln]}
                pending = []
            elif ln.strip():
                pending.append(ln)
            else:
                pending = []
            continue
        cur["lines"].append(ln)
        if re.match(r"^END_(FUNCTION_BLOCK|FUNCTION|PROGRAM|TYPE|INTERFACE)\b", ln):
            objs.append(cur)
            cur = None
    if cur is not None:
        sys.exit(f"{stem}: {cur['kind']} {cur['name']} has no END_ line")
    return objs


def pou_parts(lines):
    """(declaration, implementation): the declaration ends at the last END_VAR (or the header line)."""
    body = [l for l in lines if not POU_END.match(l)]
    ends = [i for i, l in enumerate(body) if re.match(r"^\s*END_VAR\b", l)]
    head = next(i for i, l in enumerate(body) if START.match(l))
    last = ends[-1] if ends else head
    return "\n".join(body[:last + 1]) + "\n", "\n".join(body[last + 1:]).strip("\n") + "\n"


def element_for(obj):
    text = "\n".join(obj["lines"]) + "\n"
    if obj["kind"] == "TYPE":
        return {"name": obj["name"], "elementType": "DUT", "elementProperties": BUILD_PROPS, "declaration": text}
    if obj["kind"] == "GVL":
        return {"name": obj["name"], "elementType": "GVL", "elementProperties": BUILD_PROPS, "declaration": text}
    if obj["kind"] == "INTERFACE":
        decl = "\n".join(l for l in obj["lines"] if not l.startswith("END_INTERFACE")) + "\n"
        return {"name": obj["name"], "elementType": "ITF", "elementProperties": BUILD_PROPS, "declaration": decl}
    decl, impl = pou_parts(obj["lines"])
    return {"name": obj["name"], "elementType": "POU", "elementProperties": BUILD_PROPS, "language": "ST",
            "declaration": decl, "implementation": impl, "level": "Standard"}


ORDER = {"TYPE": 0, "INTERFACE": 1, "GVL": 2, "FUNCTION": 3, "FUNCTION_BLOCK": 4, "PROGRAM": 5}


def load_objects(files):
    objs = []
    for f in files:
        with open(f, encoding="utf-8") as fh:
            objs += split_st(fh.read(), os.path.splitext(os.path.basename(f))[0])
    names = [o["name"] for o in objs]
    dup = {n for n in names if names.count(n) > 1}
    if dup:
        sys.exit(f"defined more than once: {', '.join(sorted(dup))}")
    return sorted(objs, key=lambda o: ORDER[o["kind"]])


# ----- commands -----

def cmd_push(args, app):
    prune, dry = "--prune" in args, "--dry-run" in args
    objs = load_objects([a for a in args if not a.startswith("--")])
    existing = {}
    for child in http("GET", dev(app)).get("children") or []:
        existing[child] = http("GET", dev(f"{app}/{child}")).get("elementType")
    rc = 0
    if prune:
        keep = {o["name"] for o in objs}
        for child, etype in existing.items():
            if etype in CODE_TYPES and child not in keep:
                print(f"DELETE {child} [{etype}]")
                if not dry:
                    http("DELETE", dev(f"{app}/{child}"))
    for o in objs:
        el = element_for(o)
        etype = existing.get(o["name"])
        action = "UPDATE" if etype == el["elementType"] else ("REPLACE" if etype else "CREATE")
        print(f"{action} {o['name']} [{el['elementType']}]")
        if dry:
            continue
        try:
            if action == "UPDATE":
                http("PUT", dev(f"{app}/{o['name']}"), el)
            else:
                if action == "REPLACE":
                    http("DELETE", dev(f"{app}/{o['name']}"))
                http("POST", dev(app), el)
        except ApiError as e:
            print(f"  FAILED {e}")
            rc = 1
    return rc


def cmd_task(task, prgs, app):
    path = dev(f"{app}/task-config/{task}")
    t = http("GET", path)
    t.pop("children", None)
    t.pop("id", None)
    t["pouCalls"] = []
    http("PUT", path, t)            # PUT appends to pouCalls: clear the list first
    t["pouCalls"] = [{"name": p, "comment": ""} for p in prgs]
    r = http("PUT", path, t)
    print(json.dumps(r.get("pouCalls"), indent=1))
    return 0


def lib_repo():
    r = http("GET", "library-repositories/System", timeout=120)
    return r if isinstance(r, list) else next((v for v in r.values() if isinstance(v, list)), [])


def version_key(v):
    return [int(x) if x.isdigit() else 0 for x in v.split(".")]


def cmd_lib_add(name, version, app):
    cands = [l for l in lib_repo() if l["name"].lower() == name.lower()]
    if version:
        cands = [l for l in cands if l["version"] == version]
    if not cands:
        sys.exit(f"{name} {version or ''} not in the System repository (try lib-find)")
    lib = max(cands, key=lambda l: version_key(l["version"]))
    r = http("POST", dev(f"{app}/library-manager"), dict(lib, elementType="Library"))
    print(r.get("displayName"), "-", r.get("resolutionInfo"))
    return 0


def tree(path, depth, indent=0):
    el = http("GET", dev(path))
    print(f"{'  ' * indent}{path.rsplit('/', 1)[-1]} [{el.get('elementType')}]")
    if depth > 0:
        for c in el.get("children") or []:
            if el.get("elementType") == "LibraryManager":
                print(f"{'  ' * (indent + 1)}{c} [Library]")
            else:
                tree(f"{path}/{c}", depth - 1, indent + 1)


def opt(args, name, default=None):
    if name in args:
        i = args.index(name)
        v = args[i + 1]
        del args[i:i + 2]
        return v
    return default


def main(argv):
    args = list(argv)
    app = opt(args, "--app", APP)
    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    cmd, rest = args[0], args[1:]
    try:
        if cmd == "info":
            print(json.dumps({"product": http("GET", "product/info"), "project": http("GET", "projects/current")},
                             indent=1))
        elif cmd == "tree":
            depth = int(opt(rest, "--depth", "20"))
            tree(rest[0] if rest else "Device", depth)
        elif cmd == "get":
            el = http("GET", dev(rest[0]))
            if "--code" in rest:
                print(el.get("declaration") or "")
                if el.get("implementation") is not None:
                    print("// ---- implementation ----")
                    print(el["implementation"])
            else:
                print(json.dumps(el, indent=1))
        elif cmd == "push":
            return cmd_push(rest, app)
        elif cmd == "delete":
            http("DELETE", dev(rest[0] if "/" in rest[0] else f"{app}/{rest[0]}"))
            print("deleted", rest[0])
        elif cmd == "task":
            return cmd_task(rest[0], rest[1:], app)
        elif cmd == "lib-find":
            for l in lib_repo():
                if rest[0].lower() in json.dumps(l).lower():
                    print(f"{l['name']} {l['version']} ({l.get('company')}) placeholder={l.get('placeholderName')}")
        elif cmd == "lib-add":
            return cmd_lib_add(rest[0], rest[1] if len(rest) > 1 else None, app)
        elif cmd == "lib-rm":
            http("DELETE", dev(f"{app}/library-manager/{rest[0]}"))
            print("removed", rest[0])
        elif cmd == "build":
            return print_job(run_job({"jobType": "BuildJob", "jobParameters": {"action": "GenerateCode"}}))
        elif cmd == "save":
            return print_job(run_job({"jobType": "ProjectJob", "jobParameters": {"action": "Save"}}))
        elif cmd == "export-xml":
            return print_job(run_job({"jobType": "ExportPlcOpenXmlJob", "jobParameters": {
                "nodeUrl": "/" + dev(rest[0]), "filePath": rest[1], "fileName": rest[2]}}))
        elif cmd == "job":
            return print_job(run_job(json.loads(rest[0])))
        else:
            sys.exit(f"unknown command {cmd!r} (see --help)")
    except ApiError as e:
        sys.exit(str(e))
    except IndexError:
        sys.exit(f"{cmd}: missing argument (see --help)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
