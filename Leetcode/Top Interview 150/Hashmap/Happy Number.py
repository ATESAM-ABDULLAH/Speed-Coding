def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """

    loop = set()
    while n not in loop:
        print(f"{n}, {loop}")
        loop.add(n)
        n = sum([int(i) * int(i) for i in str(n)])
        if n == 1:  # happy number
            return True

    return False


n = 19
print(isHappy(n))
