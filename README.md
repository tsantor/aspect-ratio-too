# Aspect Ratio Too

![Coverage](https://img.shields.io/badge/coverage-100.0%25-brightgreen)

## Overview

Aspect ratio calculations.

## Installation

```bash
uv add aspect-ratio-too
```

## Usage

Know the aspect ratio you want but do not know the corresponding width/height? Try this:

```python
from aspect_ratio_too import AspectRatioCalculator

arc = AspectRatioCalculator(16, 9)

# Get (width/height) tuple
arc.width_to_dimensions(1920)  # (1920, 1080)
arc.height_to_dimensions(1080)  # (1920, 1080)

arc.width_to_height(1920)  # 1080
arc.height_to_width(1080)  # 1920
```

Or calculate the aspect ratio given known pixel dimensions:

```python
from aspect_ratio_too import aspect_ratio, aspect_ratio_str

aspect_ratio(1920, 1080)  # 1.7777777777777777
aspect_ratio_str(1920, 1080)  # 16:9
```

## Development

```bash
just --list
just env
just uv-install-dev
just pip-install-editable
```

## Testing

```bash
just pytest
just coverage
just open-coverage
```

For quick local quality checks:

```bash
just check
```

## Issues

If you experience any issues, please create one in the
[issue tracker](https://bitbucket.org/xstudios/aspect-ratio-too/issues).
