# Ideas from similar projects

Read 2026-10-30. For each step: how other projects do it, and what we use.

Projects read: autoshorts (upload-post-skills), MoneyPrinterTurbo, SlopGen, AutoShortAi,
slideshow-automation, vmashd, hdsa2019doc, mikhin's many-reels gist.

## 1. Pick random videos

| Project | How it does it |
|---|---|
| SlopGen | Picks a random file it hasn't used yet in this run. If all are used, allows repeats instead of failing |
| MoneyPrinterTurbo | Puts one piece from each different video first, so the same video doesn't show up twice |
| mikhin | Skips videos shorter than one clip |
| vmashd, hdsa2019doc | Plain random choice, repeats allowed |

**We use:** list the videos, skip any too short to clip (mikhin), then pick a few different ones
at random with no repeats (SlopGen, MoneyPrinterTurbo). If there are fewer videos than asked
for, use all of them.

## 2. Clip each one

| Project | How it does it |
|---|---|
| hdsa2019doc, vmashd | Random start point inside each video |
| mikhin | Always starts at second 0, so every clip looks the same each run |
| autoshorts | Seeks first, then re-encodes, so the cut lands on the exact frame (copying snaps to the nearest keyframe and can be off by seconds) |
| MoneyPrinterTurbo, SlopGen | Make it vertical by zooming until it fills the frame, then cutting off the overflow |
| MoneyPrinterTurbo | Forces standard colors (bt709) so clips from different phones don't shift color |
| mikhin, SlopGen | Same frame rate, same pixel shape for every clip, sound dropped |

**We use:** random start (hdsa2019doc), exact cut (autoshorts), fill-and-crop to vertical
(MoneyPrinterTurbo, SlopGen), standard colors (MoneyPrinterTurbo), same frame rate and shape
(SlopGen). All in one ffmpeg command per clip.

## 3. Combine them

| Project | How it does it |
|---|---|
| mikhin, MoneyPrinterTurbo | Write a list file, join with ffmpeg's concat |
| SlopGen | Found that the fast "copy" join can silently drop frames at the seams and come out seconds short with no error. Switched to a join that decodes, then measures the result and stops if it's short |
| AutoShortAi | Checks the output file exists and isn't empty |

**We use:** SlopGen's decoding join, plus a length check at the end (SlopGen, AutoShortAi).

## Avoided

MoviePy and ImageMagick (vmashd, hdsa2019doc): the part that broke most in the projects that used
them. We call ffmpeg directly.
