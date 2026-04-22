from __future__ import annotations

from typing import TYPE_CHECKING

import click
from rich.console import Console

from .aspect_ratio import AspectRatioCalculator
from .aspect_ratio import aspect_ratio
from .aspect_ratio import aspect_ratio_str

if TYPE_CHECKING:
    from collections.abc import Sequence

console = Console(highlight=False, markup=False)


def _calculator(ratio_width: int, ratio_height: int) -> AspectRatioCalculator:
    return AspectRatioCalculator(ratio_width, ratio_height)


@click.group()
@click.version_option()
def cli() -> None:
    """Aspect ratio calculations from the command line."""


@cli.command("ratio")
@click.argument("width", type=click.IntRange(min=1))
@click.argument("height", type=click.IntRange(min=1))
def ratio_command(width: int, height: int) -> None:
    console.print(str(aspect_ratio(width, height)))


@cli.command("ratio-str")
@click.argument("width", type=click.IntRange(min=1))
@click.argument("height", type=click.IntRange(min=1))
def ratio_str_command(width: int, height: int) -> None:
    console.print(aspect_ratio_str(width, height))


@cli.command("width-to-height")
@click.argument("ratio_width", type=click.IntRange(min=1))
@click.argument("ratio_height", type=click.IntRange(min=1))
@click.argument("width", type=click.IntRange(min=1))
def width_to_height_command(ratio_width: int, ratio_height: int, width: int) -> None:
    calculator = _calculator(ratio_width, ratio_height)
    console.print(str(calculator.width_to_height(width)))


@cli.command("height-to-width")
@click.argument("ratio_width", type=click.IntRange(min=1))
@click.argument("ratio_height", type=click.IntRange(min=1))
@click.argument("height", type=click.IntRange(min=1))
def height_to_width_command(ratio_width: int, ratio_height: int, height: int) -> None:
    calculator = _calculator(ratio_width, ratio_height)
    console.print(str(calculator.height_to_width(height)))


@cli.command("width-to-dimensions")
@click.argument("ratio_width", type=click.IntRange(min=1))
@click.argument("ratio_height", type=click.IntRange(min=1))
@click.argument("width", type=click.IntRange(min=1))
def width_to_dimensions_command(
    ratio_width: int, ratio_height: int, width: int
) -> None:
    calculator = _calculator(ratio_width, ratio_height)
    out_width, out_height = calculator.width_to_dimensions(width)
    console.print(f"{out_width}x{out_height}")


@cli.command("height-to-dimensions")
@click.argument("ratio_width", type=click.IntRange(min=1))
@click.argument("ratio_height", type=click.IntRange(min=1))
@click.argument("height", type=click.IntRange(min=1))
def height_to_dimensions_command(
    ratio_width: int,
    ratio_height: int,
    height: int,
) -> None:
    calculator = _calculator(ratio_width, ratio_height)
    out_width, out_height = calculator.height_to_dimensions(height)
    console.print(f"{out_width}x{out_height}")


def main(args: Sequence[str] | None = None) -> int:
    try:
        cli.main(
            args=list(args) if args is not None else None,
            prog_name="aspect-ratio",
            standalone_mode=False,
        )
    except click.ClickException as exc:
        exc.show()
        return exc.exit_code
    except SystemExit as exc:
        return int(exc.code) if isinstance(exc.code, int) else 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
