# Acknowledgements

## Use of AI in this software

Parts of this skill were generated and tested with the help of Anthropic's AI models **Claude Opus 5.5** and
**Claude Sonnet 5.5**, working in Claude Code under the direction of the author.

What that covers:

- **Instructions and references:** `SKILL.md`, the README and the reference notes were drafted or edited with the models.
- **Code:** the Structured Text conventions and patterns, the PLCopenXML converter and the other scripts under `scripts/` were written or revised by the models from the author's requests.
- **Testing:** the models wrote and ran tests where this repo has them, ran the tools against real ctrlX software or
  a simulator, and helped investigate and fix the problems that turned up.

The author set the requirements, directed the work, ran it on real ctrlX installations and decided what was kept.
AI-assisted work can still contain mistakes. Review generated PLC code before you rely on it, and test it on a simulator before it runs on a machine that can move or hurt something.

## Other software and trademarks

The files in `references/libs/` and `references/motion/` are generated from public Bosch Rexroth manuals ("ctrlX PLC Engineering, PLC Libraries 03VRS, Reference Book", R911430583, and "ctrlX Motion App Version 4, Application Manual", R911430551) and remain the property of Bosch Rexroth AG. `references/plc-engineering-api-v2.json` is Bosch Rexroth AG's description of the ctrlX WORKS PLC Engineering API (version 2.11.0) and also remains theirs. Both are included for reference only; see the originals for their terms. The schema check uses `lxml`, and the manual references are regenerated with poppler-utils and mupdf-tools.

ctrlX, ctrlX CORE, ctrlX DRIVE, ctrlX OS and ctrlX PLC Engineering are products of Bosch Rexroth AG, and CODESYS
is a product of CODESYS GmbH. This project is independent and is not affiliated with or endorsed by either, or by
Anthropic.

This repository is licensed under the MIT License, except for that Bosch Rexroth content, see [LICENSE](LICENSE). It comes without warranty of any kind.
