# ctrlx-engineer

A [Claude Code](https://claude.com/claude-code) skill for writing PLC code in IEC 61131-3 Structured Text for Bosch Rexroth **ctrlX CORE** (ctrlX PLC Engineering) and other CODESYS V3 controllers.

With it, Claude writes paste-ready POUs (programs, function blocks, functions), DUTs and GVLs in a fixed house style. It can also build the result into a PLCopenXML file for **Project → Import PLCopenXML…**. It covers sequences and state machines, ctrlX MOTION (MC_/ML_ commands), Data Layer real-time memory maps, I/O, alarms, interlocks, scaling and more, and it looks up the ctrlX library and Motion App manuals as it goes.

For ladder diagram (LD), install [codesys-lad](https://github.com/rduffy190/CtrlxLadderSkill) next to this skill.

## Install

Clone into your Claude Code skills folder, under this exact name:

```bash
git clone git@github.com:rduffy190/CtrlxPlcSkill.git ~/.claude/skills/ctrlx-engineer
```

Claude Code picks the skill up automatically. Ask for PLC logic ("write a function block for a pump with run feedback") and it's used.

Optional companions, cloned next to it:

| Skill | Folder | Adds |
|---|---|---|
| [codesys-lad](https://github.com/rduffy190/CtrlxLadderSkill) | `~/.claude/skills/codesys-lad` | Ladder (LD) POUs, built through this skill's converter |
| ctrlx-rest | `~/.claude/skills/ctrlx-rest` | Reading a live controller's Data Layer (node paths, RT memory maps) |

## Requirements

- Python 3.10+. The converter uses only the standard library.
- `lxml` for the schema check (`pip install lxml`).
- poppler-utils and mupdf-tools, only to regenerate the manual references.

## What's inside

| Path | Contents |
|---|---|
| `SKILL.md` | The skill: design rules, house sequence structure, output format, when to read what |
| `references/conventions.md` | Naming and style (prefixes, var block order) |
| `references/patterns.md` | Sequence template (jumps, transitions, on change, cyclic) and common building blocks |
| `references/motion-essentials.md`, `references/motion/` | ctrlX MOTION: PLC interfaces, command handling, Motion App manual chapters 4–7 |
| `references/libs/` | ctrlX PLC Libraries reference book, one file per library, with an `INDEX.md` |
| `references/datalayer-rt.md` | Reading Data Layer RT nodes and memory maps |
| `references/plcopenxml.md` | The PLCopenXML format as CODESYS and ctrlX PLC Engineering write it |
| `references/examples/FB_AxisCtrl.st` | A ready ctrlX MC_ axis wrapper in ST (power, move, halt, reset, latched diagnosis) |
| `scripts/st_to_plcopenxml.py` | Builds `.st` sources (POUs, DUTs, GVLs, and ladder POUs via codesys-lad) into one import file |
| `scripts/validate_plcopen.py` | Checks a PLCopenXML file against the PLCopen TC6 schema (downloads it once) |
| `scripts/pdf_to_libref.py` | Regenerates `references/libs/` and `references/motion/` from the Rexroth PDFs |
| `tests/run.sh`, `tests/fixtures/` | Regression suite: converter fixtures checked structurally and against the schema, the shipped example, and (when the PDFs are in `docs/`) a byte-for-byte check that the references regenerate identically |

## Building an import file yourself

```bash
python3 ~/.claude/skills/ctrlx-engineer/scripts/st_to_plcopenxml.py E_State.st GVL_IO.st FB_Pump.st PRG_Main.st -o Project.xml
python3 ~/.claude/skills/ctrlx-engineer/scripts/validate_plcopen.py Project.xml
```

Each `.st` file holds full source with the `END_...` keywords. A GVL file is named after the GVL.

## Tests

```bash
~/.claude/skills/ctrlx-engineer/tests/run.sh      # should end with ALL OK
```

## Regenerating the manual references

The source PDFs aren't in the repo (45 MB). Download "ctrlX PLC Engineering, PLC Libraries 03VRS, Reference Book" (R911430583) and "ctrlX Motion App Version 4, Application Manual" (R911430551) from Bosch Rexroth into `docs/`, then run the commands in the **Regenerating the references** section of `SKILL.md`.

## License

MIT, except `references/libs/` and `references/motion/`, which are generated from Bosch Rexroth manuals and remain their property. See [LICENSE](LICENSE).
