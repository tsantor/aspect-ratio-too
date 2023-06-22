# Aspect Ratio Too


## Overview
Aspect ratio calculations.

## Installation

    pip install aspect-ratio-too



## Development

    make env
    make reqs
    pip install -e .

## Testing

    pytest


## Usage
Know the aspect ratio you want but don't know the corresponding width/height? Try this:

    from aspect_ratio_too import AspectRatioCalculator

    arc = AspectRatioCalculator(16, 9)

    # Get (width/height) tuple
    arc.width_to_dimensions(1920)  # (1920, 1080)
    arc.height_to_dimensions(1080)  # (1920, 1080)

    arc.width_to_height(1920)  # 1080
    arc.height_to_width(1080)  # 1920

Or calculate the aspect ratio given know pixel dimensions:

    from aspect_ratio_too import aspect_ratio, aspect_ratio_str

    aspect_ratio(1920, 1080)  # 1.7777777777777777

    aspect_ratio_str(1920, 1080)  # 16:9


## Issues

If you experience any issues, please create an [issue](https://bitbucket.org/xstudios/aspect-ratio-too/issues) on Bitbucket.
