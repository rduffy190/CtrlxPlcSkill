"""Offline test of scripts/plceng.py against tests/mock_plceng.py (no ctrlX WORKS needed)."""
import json
import os
import socket
import subprocess
import sys
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(HERE, "..", "scripts", "plceng.py")
FIX = os.path.join(HERE, "fixtures")
APP = "Device/Plc Logic/Application"

s = socket.socket()
s.bind(("127.0.0.1", 0))
port = s.getsockname()[1]
s.close()
mock = subprocess.Popen([sys.executable, os.path.join(HERE, "mock_plceng.py"), str(port)], stdout=subprocess.PIPE, text=True)
mock.stdout.readline()
env = dict(os.environ, PLCENG_URL=f"http://127.0.0.1:{port}")
fails = 0


def run(*args, ok=True):
    r = subprocess.run([sys.executable, "-I", P, *args], env=env, capture_output=True, text=True)
    if ok and r.returncode:
        print(r.stdout, r.stderr)
    return r


def check(name, cond, detail=""):
    global fails
    print(("PASS " if cond else "FAIL ") + name + ("" if cond else f"  {detail}"))
    fails += not cond


def get(path):
    with urllib.request.urlopen(f"http://127.0.0.1:{port}/plc/engineering/api/v2/devices/"
                                + urllib.parse.quote(path)) as r:
        return json.load(r)


try:
    files = [os.path.join(FIX, f) for f in ("Types.st", "GVL_Test.st", "POUs.st")]
    r = run("push", *files, "--prune")
    out = r.stdout
    check("push: exit 0", r.returncode == 0, r.stderr)
    check("push --prune deletes code not in the files", "DELETE PRG_Old [POU]" in out, out)
    check("push --prune keeps folders, tasks, libraries", "CheckFunctions" in get(APP)["children"]
          and "task-config" in get(APP)["children"])
    check("push replaces an object of another type", "REPLACE Fn_Add [POU]" in out, out)
    check("push creates DUT/GVL/POU", all(s in out for s in ("CREATE E_TestState [DUT]", "CREATE GVL_Test [GVL]",
                                                              "CREATE FB_All [POU]", "CREATE PRG_Test [POU]")), out)
    check("push order: types before GVLs before POUs",
          out.index("E_TestState") < out.index("GVL_Test") < out.index("Fn_Add") < out.index("FB_All") < out.index("PRG_Test"))
    fb = get(f"{APP}/FB_All")
    check("POU declaration keeps the header comment and ends at END_VAR",
          fb["declaration"].startswith("// FB_All") and fb["declaration"].rstrip().endswith("END_VAR"), fb["declaration"][:80])
    check("POU implementation has no END_FUNCTION_BLOCK", "END_FUNCTION_BLOCK" not in fb["implementation"]
          and fb["implementation"].strip() != "")
    check("DUT keeps END_TYPE", get(f"{APP}/ST_Pair")["declaration"].rstrip().endswith("END_TYPE"))
    r = run("push", *files)
    check("second push updates in place", "UPDATE FB_All [POU]" in r.stdout and "CREATE" not in r.stdout, r.stdout)

    r = run("task", "MainTask", "PRG_Test")
    calls = get(f"{APP}/task-config/MainTask")["pouCalls"]
    check("task replaces the call list (PUT appends)", [c["name"] for c in calls] == ["PRG_Test"], calls)

    r = run("lib-add", "CXA_Test")
    check("lib-add picks the newest version", "4.10.0.0" in json.dumps(get(f"{APP}/library-manager/CXA_TEST")), r.stdout)
    r = run("lib-rm", "CXA_TEST")
    check("lib-rm by placeholder", "CXA_TEST" not in get(f"{APP}/library-manager")["children"])

    r = run("build")
    check("build waits for the job and prints the result", r.returncode == 0 and "0 errors" in r.stdout, r.stdout)
    r = run("get", f"{APP}/NoSuchPou", ok=False)
    check("missing element: error with the server's description", r.returncode and "not found in project" in r.stderr, r.stderr)
    r = subprocess.run([sys.executable, "-I", P, "info"], capture_output=True, text=True,
                       env={k: v for k, v in env.items() if k != "PLCENG_URL"})
    check("no PLCENG_URL: asks for the engineering PC's IP", r.returncode and "ask the user for the IP" in r.stderr, r.stderr)
    r = subprocess.run([sys.executable, "-I", P, "info"], capture_output=True, text=True,
                       env=dict(env, PLCENG_URL="127.0.0.1:1"))
    check("unreachable API: offers the reverse SSH tunnel", r.returncode and "ssh -N -R 1:localhost:1 " in r.stderr, r.stderr)
    r = subprocess.run([sys.executable, "-I", P, "info"], capture_output=True, text=True,
                       env=dict(env, PLCENG_URL=f"127.0.0.1:{port}"))
    check("bare <ip>:<port> is accepted", r.returncode == 0 and "4.6.2" in r.stdout, r.stderr)
finally:
    mock.terminate()

sys.exit(1 if fails else 0)
