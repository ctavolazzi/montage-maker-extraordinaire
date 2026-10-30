# How to work in this repo

CT (Christopher) owns this. It is a small tool: folder of clips in, captioned vertical video out.

## Rules

- **Simple first.** One feature list (`docs/PLAN.md`). Anything not on it goes under "Not in v1"
  until CT asks for it.
- **ffmpeg does the video work.** Call it through `subprocess`. Do not add MoviePy, ImageMagick,
  or a GUI framework.
- **Pillow draws text.** Never use ffmpeg's `drawtext` filter (needs a libfreetype build that is
  often missing).
- **Never touch the user's originals.** Read from `clips/`, write only to `ready/` and `.montage/`.
- **Borrowed code keeps its credit.** Anything adapted from another repo says where it came from
  in a comment, with the license (see `docs/PRIOR-ART.md`). Only copy code from repos with a
  license that allows it; for unlicensed repos, borrow the idea, not the code.
- **No em dashes** in code comments, docs or output text.
- Commits go to `main`, small, plain messages. Don't open or watch pull requests unless CT asks.
