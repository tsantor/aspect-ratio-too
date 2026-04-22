from __future__ import annotations

import importlib
import sys
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Sequence

_MISSING_CLI_DEPS_MESSAGE = (
    "The aspect-ratio CLI requires optional dependencies.\n"
    'Install them with: pip install "aspect-ratio-too[cli]"'
)


def main(args: Sequence[str] | None = None) -> int:
    try:
        cli_module = importlib.import_module("aspect_ratio_too.cli")
    except ModuleNotFoundError as exc:
        if exc.name in {"click", "rich"}:
            sys.stderr.write(f"{_MISSING_CLI_DEPS_MESSAGE}\n")
            return 1
        raise

    return cli_module.main(args)
