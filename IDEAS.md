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

## 4. How long each clip is (researched 2026-11-01)

| Source | What it says | What we do with it |
|---|---|---|
| Cutting et al., "Quicker, faster, darker", *i-Perception* 2011 ([link](https://pmc.ncbi.nlm.nih.gov/articles/PMC3485803/)) | Average shot length in Hollywood fell from about 10 s (1930s) to under 4 s after 2000. Shot lengths are skewed (a few long, many short). In modern films shorter shots carry more motion (r = -0.46, strongest in action and comedy) | Clip lengths drawn from a skewed (log-normal) spread around 2 s, between 1 and 4.5 s. Busier clips get shorter, calmer ones longer |
| Larry Jordan, via No Film School ([link](https://nofilmschool.com/2014/09/larry-jordan-teaches-us-how-create-video-montage-set-music)) | Make shots different lengths: identical lengths make a predictable rhythm and viewers start anticipating the cuts | Never all the same length |
| Eisenstein's methods of montage, via PremiumBeat ([link](https://www.premiumbeat.com/blog/soviet-montage-theory-types)) | "Metric" cuts to a fixed count and feels mechanical; "rhythmic" sets each shot's length by what's in it, and is how most editing is done today | Length follows the content of each clip (its movement), not a fixed count |
| Walter Murch's Rule of Six, via StudioBinder ([link](https://www.studiobinder.com/blog/walter-murch-rule-of-six/)) | Cut for emotion first, then story, then rhythm | Not automatable yet; noted for a later AI step |
| Kapwing, short-form video statistics 2026 ([link](https://www.kapwing.com/resources/short-form-video-statistics-tiktok-reels-and-shorts-by-the-numbers-in-2026/)) | 15 to 30 s Reels averaged 5.8% engagement; 21 to 34 s cited as best. About 65% of people who watch the first 3 s stay for 10 s (Facebook IQ) | About 20 s total. The busiest clip goes first and is kept short (1.5 s at most) as the hook |

## 5. On-screen text

CT's rule (2026-10-30): text on real things (a mug) is fine. Screenshots, screen recordings,
and text in the top half (where his caption goes) are not.

A free 2.4 MB text-finding model (OpenCV model zoo, PP-OCRv3, Apache 2.0) checks each video
cropped to vertical, once a second. Level text sitting still in the top half is avoided. A
frame with 4 or more level text boxes, or text covering more than 3% of it, counts as a
screen; a video that is a screen for more than half its frames is skipped. Tested on CT's
Drive videos: the mug video passed, an Instagram story recording and a tweet screenshot were
skipped.

## Avoided

MoviePy and ImageMagick (vmashd, hdsa2019doc): the part that broke most in the projects that used
them. We call ffmpeg directly.
