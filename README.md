# ctrlx-engineer

An agent skill (`SKILL.md` format) for writing PLC code in IEC 61131-3 Structured Text for Bosch Rexroth **ctrlX CORE** (ctrlX PLC Engineering) and other CODESYS V3 controllers.

An agent using it writes paste-ready POUs (programs, function blocks, functions), DUTs and GVLs in a fixed house style. It can also build the result into a PLCopenXML file for **Project → Import PLCopenXML…**, or push it into an open ctrlX PLC Engineering project over its REST API. It covers sequences and state machines, ctrlX MOTION (MC_/ML_ commands), Data Layer real-time memory maps, I/O, alarms, interlocks, scaling and more, and it looks up the ctrlX library and Motion App manuals as it goes.

## Install

Put this folder in the skills directory your agent loads skills from, under the folder name `ctrlx-engineer`. The agent picks it up from the `SKILL.md` description when asked for PLC logic ("write a function block for a pump with run feedback").

The scripts also work on their own, without an agent (see below).

Companion skills, installed in the same skills directory:

| Skill | Adds |
|---|---|
| `codesys-lad` | Ladder (LD) POUs, built through this skill's converter. Needs this skill next to it. |
| `ctrlx-rest` | Reading a live controller's Data Layer (node paths, RT memory maps) and configuring axes |
| `ctrlx-hmi` | WebVisu screens for the Cmd/Sts structs this skill writes |

## Requirements

- Python 3.10+. The converter uses only the standard library. (On Windows, run the scripts with `python` or `py -3` where the docs say `python3`.)
- `lxml` for the schema check (`pip install lxml`).
- poppler-utils and mupdf-tools, only to regenerate the manual references.

## What's inside

| Path | Contents |
|---|---|
| `SKILL.md` | The skill: design rules, house sequence structure, output format, when to read what |
| `references/conventions.md` | Naming and style (prefixes, var block order) |
| `references/patterns.md` | Sequence template (transitions, jumps, on change, cyclic) and common building blocks |
| `references/platforms.md` | Differences between ctrlX CORE and other CODESYS targets |
| `references/motion-essentials.md`, `references/motion/` | ctrlX MOTION: PLC interfaces, command handling, Motion App manual chapters 4–7 |
| `references/libs/` | ctrlX PLC Libraries reference book, one file per library, with an `INDEX.md` |
| `references/datalayer-rt.md` | Reading Data Layer RT nodes and memory maps from the PLC |
| `references/plcopenxml.md` | The PLCopenXML format as CODESYS and ctrlX PLC Engineering write it |
| `references/plc-engineering-api.md`, `-v2.json` | PLC Engineering REST API notes and its OpenAPI spec |
| `references/examples/FB_AxisCtrl.st`, `ST_Dynamics.st` | A ready ctrlX MC_ axis wrapper in ST (power, move, halt, reset, latched diagnosis) and the type it needs |
| `scripts/st_to_plcopenxml.py` | Builds `.st` sources (POUs, DUTs, GVLs, and ladder POUs via codesys-lad) into one import file |
| `scripts/validate_plcopen.py` | Checks a PLCopenXML file against the PLCopen TC6 schema (downloads it once) |
| `scripts/plceng.py` | PLC Engineering REST API client: push ST, add libraries and task calls, build, save |
| `scripts/pdf_to_libref.py` | Regenerates `references/libs/` and `references/motion/` from the Rexroth PDFs |
| `tests/run.sh`, `tests/fixtures/` | Regression suite: converter fixtures checked structurally and against the schema, the shipped example, `plceng.py` against a mock server, and (when the PDFs are in `docs/`) a byte-for-byte check that the references regenerate identically |

## Building an import file yourself

```bash
python3 <skills-dir>/ctrlx-engineer/scripts/st_to_plcopenxml.py E_State.st GVL_IO.st FB_Pump.st PRG_Main.st -o Project.xml
python3 <skills-dir>/ctrlx-engineer/scripts/validate_plcopen.py Project.xml
```

Each `.st` file holds full source with the `END_...` keywords. A GVL file is named after the GVL.

## Tests

```bash
<skills-dir>/ctrlx-engineer/tests/run.sh      # should end with ALL OK (bash; Git Bash on Windows)
```

## Regenerating the manual references

The source PDFs aren't in the repo (45 MB). Download "ctrlX PLC Engineering, PLC Libraries 03VRS, Reference Book" (R911430583) and "ctrlX Motion App Version 4, Application Manual" (R911430551) from Bosch Rexroth into `docs/`, then run the commands in the **Regenerating the references** section of `SKILL.md`.

## License

MIT, except `references/libs/`, `references/motion/` (generated from Bosch Rexroth manuals) and `references/plc-engineering-api-v2.json` (Bosch Rexroth's API description), which remain their property. See [LICENSE](LICENSE).

Parts of this skill were generated and tested with Claude Opus 5.5 and Claude Sonnet 5.5, see [ACKNOWLEDGEMENTS.md](ACKNOWLEDGEMENTS.md).

