from audioop import reverse


def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    mapping = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M",
    }
    it = list(mapping.items())
    it.sort(reverse=True)
    res = ""
    for n, ch in it:
        if num >= n:
            res += ch * (num // n)  # no of same rom numerals
            num %= n  # decrease num
    return res


i = 890
print(f"{i} = ", intToRoman(i))
