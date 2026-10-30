# Prior art

Existing tools found 2026-10-30. For the six marked "code read", the source was cloned and
read (not run). The rest were judged from their own pages only.

## Code read

| Repo (commit read) | License | How it picks clips | How it captions | Take from it |
|---|---|---|---|---|
| [upload-post/upload-post-skills](https://github.com/upload-post/upload-post-skills), `skills/autoshorts/autoshorts.py` (`935ea6f`) | MIT | One long video per run. Tracks used files by SHA-256 in a state file; each file used once per "cycle"; when all are used a new cycle starts. Newest unused file wins | `render_hook_png`: Pillow draws wrapped text into a transparent PNG, white fill, 3 px black stroke, rounded black pill (alpha 200) behind each line. ffmpeg `overlay` puts it at `H*0.08`. Comment says this avoids `drawtext`, which needs libfreetype | **Caption renderer (adapt nearly as is, keep credit). Cycle tracking idea.** |
| [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo), `app/services/video.py` (`27843a9`) | MIT | `combine_videos`: chops every source into chunks of `max_clip_duration`, shuffles, prefers chunks from different source files | Subtitles from TTS or Whisper, not used here | **Cover-and-crop to 9:16** (scale by the larger of the two ratios, center crop). Prefer-unique-sources idea |
| [boonej/vmashd](https://github.com/boonej/vmashd), `src/vmashd/videoutility.py` (`17de71f`) | MIT | Random start inside each clip; "weights" long videos so they appear more | MoviePy `TextClip` on about 20% of clips, random line from a text file | Idea of a captions file. **Bug:** `weight_videos` appends `v[it]` (the first few videos) instead of `v[i]`, so it weights the wrong clips. Loads every video into memory at once |
| [hackersanddesigners/hdsa2019doc](https://github.com/hackersanddesigners/hdsa2019doc), `generate.py` (`5f09ab0`) | none found | `random.choice` file, random length 1 to max, random start; repeats allowed; loops until duration filled | MoviePy `TextClip` (needs ImageMagick; README has a font workaround section) | Random start and length idea only (no license, so no code) |
| [mikhin's many-reels.js gist](https://gist.github.com/mikhin/3abf12ab5a9965f167197d239cf275d8) | none stated | Random files, no repeats within a video, but always cuts from second 0 | None | Re-encode every segment at `-r 30` before `-f concat -safe 0`, then add music with `-shortest`. Batch loop (`numberOfVideos`). Ideas only |
| [michael-sutu/Video-Generator](https://github.com/michael-sutu/Video-Generator) | none found | "Random" is picking between 2 hardcoded videos in the browser | Draws on a browser canvas and records it with MediaRecorder; depends on outside APIs | Nothing |
| [coopcz/slideshow-automation](https://github.com/coopcz/slideshow-automation) | none found | Not random: AI describes each image, then ranks images by match to each slide's text; tracks recent use | Canvas compositor | v2 idea: pick clips that fit the caption |

## Lessons

- Every fragile part seen was MoviePy plus ImageMagick (fonts, install). Use ffmpeg directly.
- Draw text with Pillow, overlay with ffmpeg. Skip `drawtext`.
- Normalize every slice (size, fps, pixel format) before concat or the concat breaks.
- Track used clips by content hash, not file name, so renamed files still count.

## Products (not code read)

Closest finished products: UGCDock (splits recordings, remixes, captions, schedules),
repli.ac (free, local-first, caption variations, batch export). Also: UGCdrop Studio,
Remix Studio, ClipForge, CapCut AutoCut, Picsart Reeva, Reelful, GoPro Quik, Google Photos
highlight videos, FirstCut Studio. Slideshow-only: ReelFarm, ReelFlood, ReelMoney, Plannic.
Render APIs for a no-code version: Creatomate, Shotstack, JSON2Video, Orshot (with n8n or Make).
None of them pull directly from a phone camera roll at random.
