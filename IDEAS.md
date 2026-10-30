# Ideas we took

From reading the code of similar projects, 2026-10-30.

| Project | Idea we use |
|---|---|
| [autoshorts](https://github.com/upload-post/upload-post-skills) | Draw the text as an image with Pillow, then lay it over the video. White text, black outline, dark rounded box behind it so it's readable on anything |
| [MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | Make any clip vertical: zoom until it fills the frame, cut off the edges |
| [hdsa2019doc](https://github.com/hackersanddesigners/hdsa2019doc) | Pick a random starting point in each clip, not always the beginning |
| [mikhin's gist](https://gist.github.com/mikhin/3abf12ab5a9965f167197d239cf275d8) | Convert every piece to the same size and frame rate before stitching, or stitching breaks |
| [vmashd](https://github.com/boonej/vmashd) | Skip clips that are too short |

What we avoid: MoviePy and ImageMagick. They were the part that broke most in the projects
that used them. We call ffmpeg directly instead.
