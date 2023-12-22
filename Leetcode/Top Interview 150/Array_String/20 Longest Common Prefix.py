def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    prefix = ""
    min_word = min(strs, key=len)  # smallest word in list
    for i, char in enumerate(min_word):  # loop over smalest words letters
        for word in strs:  # loop over other words
            if char != word[i]:  # any mismatch in letters of same index
                return prefix  # return prefix till now
        prefix += char  # add char to prefix if matches all same indexes
    return prefix


strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))
