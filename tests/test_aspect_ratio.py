from aspect_ratio_too import AspectRatioCalculator, aspect_ratio_str, aspect_ratio


def test_2160p():
    arc = AspectRatioCalculator(16, 9)
    width, height = (3840, 2160)
    assert arc.width_to_dimensions(width) == (width, height)
    assert arc.height_to_dimensions(height) == (width, height)


def test_1440p():
    arc = AspectRatioCalculator(16, 9)
    width, height = (2560, 1440)
    assert arc.width_to_dimensions(width) == (width, height)
    assert arc.height_to_dimensions(height) == (width, height)


def test_1080p():
    arc = AspectRatioCalculator(16, 9)
    width, height = (1920, 1080)
    assert arc.width_to_dimensions(width) == (width, height)
    assert arc.height_to_dimensions(height) == (width, height)


def test_720p():
    arc = AspectRatioCalculator(16, 9)
    width, height = (1280, 720)
    assert arc.width_to_dimensions(width) == (width, height)
    assert arc.height_to_dimensions(height) == (width, height)


def test_480p():
    arc = AspectRatioCalculator(16, 9)
    width, height = (854, 480)
    assert arc.width_to_dimensions(width) == (width, height)
    assert arc.height_to_dimensions(height) == (width, height)


def test_360p():
    arc = AspectRatioCalculator(16, 9)
    width, height = (640, 360)
    assert arc.width_to_dimensions(width) == (width, height)
    assert arc.height_to_dimensions(height) == (width, height)


def test_240p():
    arc = AspectRatioCalculator(16, 9)
    width, height = (426, 240)
    assert arc.width_to_dimensions(width) == (width, height)
    assert arc.height_to_dimensions(height) == (width, height)

def test_aspect_ratio():
    assert aspect_ratio(1920, 1080) == 1.7777777777777777


def test_aspect_ratio_str():
    assert aspect_ratio_str(1920, 1080) == "16:9"
