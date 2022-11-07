from math import ceil, floor


def closest_number(number, multiple):
    """Find closest number divisible by multiple."""
    # Find the quotient
    q = int(number / multiple)

    # 1st possible closest number
    n1 = multiple * q

    # 2nd possible closest number
    n2 = multiple * (q + 1) if (number * multiple) > 0 else multiple * (q - 1)

    # if true, then n1 is the required closest number
    return n1 if abs(number - n1) < abs(number - n2) else n2


def round_to_multiple(number, multiple, direction="nearest"):
    if direction == "nearest" or direction not in ["up", "down"]:
        return multiple * round(number / multiple)
    elif direction == "up":
        return multiple * ceil(number / multiple)
    elif direction == "down":
        return multiple * floor(number / multiple)
