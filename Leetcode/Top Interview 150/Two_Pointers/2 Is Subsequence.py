def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if not s:  # s = '' = True
        return True

    i = 0  # index of s
    for l in t:
        if l == s[i]:  # if s[i] found -> increase index
            i += 1
        if i == len(s):  # if all letters found
            return True
    return False  # all not found


s = "abc"
t = "ahbgdc"
print(isSubsequence(s, t))
