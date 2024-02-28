def isIsomorphic(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    map_s, map_t = {}, {}
    for a, b in zip(s, t):
        if a not in map_s:  # new letter in s
            map_s[a] = b  # add letter to mapping
        elif b != map_s[a]:  # mapping change: wrong char
            return False

        if b not in map_t:  # new letter in t
            map_t[b] = a  # add letter to mapping
        elif a != map_t[b]:  # mapping change: wrong char
            return False
        print(map_s, map_t)

    return True


s = "egg"
t = "atd"
print(isIsomorphic(s, t))
