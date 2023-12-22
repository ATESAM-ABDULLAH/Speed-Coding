def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    # Approach 1 (easier): use builtin funcs
    # return haystack.find(needle)

    # Approach 2 (faster): iterate from 0- (last-len(needle)) b/c we need to fit needle here
    for i in range(len(haystack) - len(needle) + 1):
        if (
            haystack[i : i + len(needle)] == needle
        ):  # Just check if needle exists from this position
            return i
    return -1


haystack = "a"
needle = "a"
print(strStr(haystack, needle))
