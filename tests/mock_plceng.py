"""Minimal in-memory mock of the ctrlX PLC Engineering API v2, with the real server's quirks:
PUT on a task appends pouCalls, a task call object can't be deleted (501), a duplicate POST is 400,
a missing path is 404 with a Problem JSON. Run: python3 mock_plceng.py <port>."""
import json
import os
import sys
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PREFIX = "/plc/engineering/api/v2/"


def el(name, etype, **kw):
    return dict({"name": name, "elementType": etype, "children": []}, **kw)


ROOT = el("Device", "Device")
ROOT["children"] = [el("Plc Logic", "PLCLogic")]
APP = el("Application", "Application")
ROOT["children"][0]["children"] = [APP]
TASK = el("MainTask", "Task", pouCalls=[{"name": "PRG_Old", "comment": ""}])
APP["children"] = [
    el("library-manager", "LibraryManager", children=[el("Standard", "Library")]),
    el("task-config", "TaskConfig", children=[TASK]),
    el("symbol-config", "SymbolConfig"),
    el("CheckFunctions", "Folder"),
    el("PRG_Old", "POU", language="ST", declaration="PROGRAM PRG_Old\n", implementation=""),
    el("Fn_Add", "DUT", declaration="TYPE Fn_Add : INT; END_TYPE\n"),     # wrong type: push must replace it
]
LIBS = [{"name": "CXA_Test", "version": v, "company": "Bosch Rexroth AG", "placeholderName": "CXA_TEST"}
        for v in ("4.6.0.0", "4.10.0.0", "4.6.2.0")]
JOBS = {}
PROJECT_PATH = "C:\\Mock.project"   # argv[2] overrides: a local path makes the "PC" this machine


def problem(status, kind, text):
    return status, {"severity": "Error", "type": kind, "status": status, "dynamicDescription": text}


def find(parts):
    node = {"children": [ROOT]}
    parent = None
    for p in parts:
        # libraries are addressed by their placeholder, like the real server
        nxt = next((c for c in node["children"] if p in (c["name"], c.get("placeholderName"))), None)
        if nxt is None:
            return None, None
        parent, node = node, nxt
    return parent, node


def view(node):
    v = {k: val for k, val in node.items() if k != "children"}
    v["children"] = [c["name"] for c in node["children"]]
    if node["elementType"] == "Task":
        v["children"] = [f"{c['name']}.Unknown_TaskPOUCallObject" for c in node["pouCalls"]]
    if node["elementType"] == "LibraryManager":
        v["children"] = [c.get("placeholderName") or c["name"] for c in node["children"]]
    return v


def handle(method, path, body):
    if path == "product/info":
        return 200, {"versionText": "4.6.2"}
    if path == "projects/current":
        return 200, {"name": "Mock", "path": PROJECT_PATH}
    if path == "library-repositories/System":
        return 200, {"libraries": LIBS}
    if path == "jobs" and method == "POST":
        jid = f"{len(JOBS) + 1:016x}"
        info = {"BuildJob": "Build complete -- 0 errors, 0 warnings: Ready for download.",
                "ProjectJob": "Project successfully saved."}.get(body["jobType"], "ok")
        final = "Done"
        if body["jobType"] == "ImportPlcOpenXmlJob":
            # Like the real server, the file is read from "the PC's" disk (here: this machine)
            jp = body["jobParameters"]
            f = os.path.join(jp["filePath"], jp["fileName"])
            final = "Done" if os.path.isfile(f) else "Failed"
            info = f"File '{jp['fileName']}'  successfully Imported." if final == "Done" else f"File not found: {f}"
        JOBS[jid] = dict(body, id=jid, state="Running", progress=50, jobResultInfo=info, final=final)
        return 201, {k: v for k, v in JOBS[jid].items() if k != "final"}
    if path.startswith("jobs/"):
        j = JOBS[path[5:]]
        j["state"], j["progress"] = j["final"], 100     # one poll later it's finished
        return 200, {k: v for k, v in j.items() if k != "final"}
    if not path.startswith("devices/"):
        return problem(404, "NotFound", f"no route {path}")
    parts = path[len("devices/"):].split("/")
    if parts[-1].endswith(".Unknown_TaskPOUCallObject") and method == "DELETE":
        return problem(501, "NotImplemented", f"Not yet implemented: '{parts[-1].split('.')[0]}' object cannot be deleted")
    parent, node = find(parts)
    if node is None:
        return problem(404, "NotFound", f"Path '/{'/'.join(parts)}' not found in project.")
    if method == "GET":
        return 200, view(node)
    if method == "DELETE":
        parent["children"].remove(node)
        return 200, None
    if method == "PUT":
        if node["elementType"] == "Task":
            node.update({k: v for k, v in body.items() if k != "pouCalls"})
            node["pouCalls"] = node["pouCalls"] + body["pouCalls"] if body["pouCalls"] else []
        else:
            node.update({k: v for k, v in body.items() if k != "children"})
        return 200, view(node)
    if method == "POST":
        if body.get("elementType") == "POU" and body.get("language") != "ST":
            return problem(400, "BadRequest", f"Language type '{body.get('language')}' is not supported.")
        if any(c["name"] == body["name"] for c in node["children"]):
            return problem(400, "BadRequest", f"An object with the name '{body['name']}' already exists "
                                              "within the corresponding namespace.")
        new = dict(body, children=[])
        node["children"].append(new)
        return 201, view(new)
    return problem(405, "MethodNotAllowed", method)


class H(BaseHTTPRequestHandler):
    def _do(self):
        path = urllib.parse.unquote(urllib.parse.urlsplit(self.path).path)
        if not path.startswith(PREFIX):
            status, out = problem(404, "NotFound", path)
        else:
            n = int(self.headers.get("Content-Length") or 0)
            body = json.loads(self.rfile.read(n)) if n else None
            status, out = handle(self.command, path[len(PREFIX):], body)
        raw = json.dumps(out).encode() if out is not None else b""
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    do_GET = do_PUT = do_POST = do_DELETE = _do

    def log_message(self, *a):
        pass


if __name__ == "__main__":
    if len(sys.argv) > 2:
        PROJECT_PATH = sys.argv[2]
    srv = ThreadingHTTPServer(("127.0.0.1", int(sys.argv[1])), H)
    print("ready", flush=True)
    srv.serve_forever()
