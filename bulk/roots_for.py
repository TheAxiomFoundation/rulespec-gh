#!/usr/bin/env python3
"""Print the guard-generated `--roots` for an applied module path.

`axiom-encode guard-generated --roots` wants the space-separated jurisdiction
roots that the changed files live under. rulespec-gh is a single-jurisdiction
repo: the only root is `gh`.

Usage:
  python bulk/roots_for.py gh/statutes/act-1134/x.yaml   # -> "gh"
"""

from __future__ import annotations

import sys
from pathlib import PurePosixPath


def roots_for(module_path: str) -> str:
    parts = PurePosixPath(module_path).parts
    if not parts:
        return "gh"
    juris = parts[0]
    roots = ["gh"]
    if juris != "gh" and juris.startswith("gh-"):
        roots.append(juris)
    return " ".join(dict.fromkeys(roots))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: roots_for.py <module-path>", file=sys.stderr)
        raise SystemExit(2)
    print(roots_for(sys.argv[1]))
