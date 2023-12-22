def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total, prev, curr = 0, 0, 0

    for x in s:
        curr = mapping[x]
        if curr > prev:  # Subtraction case
            total += curr - (
                2 * prev
            )  # Subtract the prev we added + reduction from current
        else:
            total += curr
        prev = curr

    return total


rom = "DDDLLLLLLLLLXLIV"
print(romanToInt(rom))
