def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    letters, l, ml = {}, 0, 0
    for r, x in enumerate(s):
        if (
            x in letters and letters[x] >= l
        ):  # repeating char -> move l to after first occurence
            l = letters[x] + 1
        else:  # valid substr -> check if largest
            ml = max(ml, r - l + 1)
        letters[x] = r  # update the index where x was found
        print(letters, l, r, ml)
    return ml


s = "tmmzuxt"
print(lengthOfLongestSubstring(s))
