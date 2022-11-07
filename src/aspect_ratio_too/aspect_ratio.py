import math
from aspect_ratio_too.utils import closest_number


def aspect_ratio_str(width: int, height: int) -> str:
    """ "Given a pixel width/height return a string ratio (eg - 16:9)."""
    r = math.gcd(width, height)
    x = int(width / r)
    y = int(height / r)
    return f"{x}:{y}"


def aspect_ratio(width: int, height: int) -> float:
    """Given width/height return aspect ratio as a percentage."""
    return width / height


class AspectRatioCalculator:

    """Calculate pixel dimensions for width/height given an aspect ratio. (eg - 16/9)."""

    def __init__(self, ratio_width: int, ratio_height: int):
        self.ratio = ratio_width / ratio_height

    def width_to_height(self, width: int) -> int:
        return closest_number(width / self.ratio, 2)

    def height_to_width(self, height: int) -> int:
        return closest_number(height * self.ratio, 2)

    def width_to_dimensions(self, width: int) -> int:
        height = self.width_to_height(width)
        return (width, height)

    def height_to_dimensions(self, height: int) -> int:
        width = self.height_to_width(height)
        return (width, height)
