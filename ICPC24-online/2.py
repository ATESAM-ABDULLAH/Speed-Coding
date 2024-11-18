def min_moves_for_symmetry(s):
    left, right = 0, len(s) - 1
    moves = 0

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            # Find the first occurrence of s[right] from the left
            found = False
            for i in range(left + 1, right + 1):
                if s[i] == s[right]:
                    found = True
                    # Create new string with swapped characters
                    new_s = (
                        s[:left]
                        + s[i]
                        + s[left + 1 : i]
                        + s[right]
                        + s[left:i]
                        + s[i + 1 :]
                    )
                    s = new_s
                    moves += 1
                    break
            if not found:
                return -1
            left += 1
            right -= 1

    return moves


# Python implementation of program
def minSwap(s):
    strng = list(s)
    unmp = {}
    for i in strng:
        unmp[i] = unmp.get(i, 0) + 1
    odd = 0
    result = 0
    left = 0
    right = len(strng) - 1
    for i in unmp:
        if unmp[i] % 2 != 0:
            odd += 1
    # If we found more than one odd number
    if odd > 1:
        return -1
    while left < right:
        l = left
        r = right
        while strng[l] != strng[r]:
            r -= 1
        if l == r:
            # When we found odd element move towards middle
            strng[r], strng[r + 1] = strng[r + 1], strng[r]
            result += 1
            continue
        else:
            # Normal element move towards right of string
            while r < right:
                strng[r], strng[r + 1] = strng[r + 1], strng[r]
                r += 1
                result += 1
        left += 1
        right -= 1
    # print(strng)
    return result


# This code is contributed by rupasriachanta421


def main():
    t = int(input())
    for _ in range(t):
        s = input()
        print(minSwap(s))


if __name__ == "__main__":
    main()
