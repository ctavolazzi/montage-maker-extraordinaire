"""Choose which clips go into the next video."""

from pathlib import Path

from . import state as st
from .config import Config


def list_clips(cfg: Config) -> list[Path]:
    """Every video file in clips_dir (top level only in v1), skipping hidden files."""
    # return [p for p in cfg.clips_dir.iterdir() if p.suffix.lower() in cfg.video_exts]
    raise NotImplementedError


def pick(cfg: Config, state: dict) -> list[Path]:
    """Return cfg.clips_per_video clips, none used this cycle, all from different files.

    Clips shorter than cfg.slice_min_s are skipped (never stretched).
    """
    # clips = [c for c in list_clips(cfg) if probe(c).duration_s >= cfg.slice_min_s]
    # if len(clips) < cfg.clips_per_video: raise SystemExit("need at least N clips in clips/")
    # available = [c for c in clips if st.is_available(state, st.file_hash(c))]
    # if len(available) < cfg.clips_per_video:
    #     st.new_cycle(state)
    #     available = clips
    # chosen = random.sample(available, cfg.clips_per_video)
    # for c in chosen: st.mark_used(state, st.file_hash(c), c.name)
    # return chosen
    raise NotImplementedError


def pick_music(cfg: Config) -> Path | None:
    """A random track from music_dir, or None if music is off or the folder is empty."""
    raise NotImplementedError


def pick_caption(cfg: Config, given: str | None) -> str | None:
    """The --caption text if given, else a random non-empty line from captions.txt, else None."""
    raise NotImplementedError
