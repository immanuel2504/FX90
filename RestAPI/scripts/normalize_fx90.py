#!/usr/bin/env python3
"""Backward-compatible entry point — use RestAPI/scripts/normalize_fxr90.py instead."""
from __future__ import annotations

import runpy
from pathlib import Path

TARGET = Path(__file__).resolve().parent.parent / "RestAPI" / "scripts" / "normalize_fxr90.py"

if __name__ == "__main__":
    runpy.run_path(str(TARGET), run_name="__main__")
