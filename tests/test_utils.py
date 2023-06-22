from aspect_ratio_too.utils import round_to_multiple

# def test_round_to_multiple():
#     assert round_to_multiple(9, 2) == 8


def test_round_to_multiple_up():
    assert round_to_multiple(9, 2, "up") == 10


def test_round_to_multiple_down():
    assert round_to_multiple(9, 2, "down") == 8


def test_round_to_multiple_nearest():
    assert round_to_multiple(9, 2, "nearest") == 8
