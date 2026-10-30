"""Which clips have been used this cycle.

Idea from upload-post/upload-post-skills autoshorts.py `cmd_pick` (MIT): track files by
content hash, use each once per cycle, start a new cycle when all are used.
"""

from pathlib import Path


def load(state_file: Path) -> dict:
    """Read state.json, or return an empty state if it doesn't exist."""
    # if not state_file.exists(): return {"cycle_started_at": now_iso(), "used": {}}
    # return json.loads(state_file.read_text())
    raise NotImplementedError


def save(state_file: Path, state: dict) -> None:
    """Write state.json atomically (write to .tmp, then rename)."""
    raise NotImplementedError


def file_hash(path: Path) -> str:
    """SHA-256 of the file. Hash the first and last 8 MB plus the size, not the whole file,
    so large phone videos hash fast. Renamed files keep the same hash."""
    raise NotImplementedError


def is_available(state: dict, h: str) -> bool:
    # rec = state["used"].get(h)
    # return rec is None or rec["last_used_at"] < state["cycle_started_at"]
    raise NotImplementedError


def mark_used(state: dict, h: str, name: str) -> None:
    # state["used"][h] = {"name": name, "last_used_at": now_iso()}
    raise NotImplementedError


def new_cycle(state: dict) -> None:
    # state["cycle_started_at"] = now_iso()
    raise NotImplementedError
