"""Command line entry point.

    montage --caption "Day 12 of building a robot farm"
    montage --count 7
    montage --clips 5 --min 2 --max 3 --no-music
"""

import argparse


def parse_args(argv=None) -> argparse.Namespace:
    p = argparse.ArgumentParser(prog="montage",
                                description="Folder of clips in, captioned vertical video out.")
    p.add_argument("--caption", help="caption text (default: random line from captions.txt)")
    p.add_argument("--count", type=int, default=1, help="how many videos to make")
    p.add_argument("--clips", type=int, help="clips per video (default 4)")
    p.add_argument("--min", type=float, help="shortest slice in seconds (default 2)")
    p.add_argument("--max", type=float, help="longest slice in seconds (default 4)")
    p.add_argument("--clips-dir", help="folder of source videos (default ./clips)")
    p.add_argument("--font", help="path to a .ttf font")
    p.add_argument("--no-music", action="store_true", help="keep it silent")
    return p.parse_args(argv)


def main(argv=None) -> None:
    # args = parse_args(argv)
    # ffmpeg.check_installed()
    # cfg = config.load(args)
    # make ready_dir and work_dir
    # state = state.load(cfg.state_file)
    #
    # for i in range(args.count):
    #     clips = pick.pick(cfg, state)
    #     text = pick.pick_caption(cfg, args.caption)
    #     music = pick.pick_music(cfg)
    #     name = f"{date}_{time}_{i+1:02d}"
    #     video, thumb = build.make_one(cfg, clips, text, music, name)
    #     state.save(cfg.state_file, state)     # save after each video so a crash keeps progress
    #     print(video, thumb)
    raise NotImplementedError


if __name__ == "__main__":
    main()
