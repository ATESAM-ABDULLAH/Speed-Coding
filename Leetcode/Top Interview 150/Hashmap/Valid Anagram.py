from collections import Counter


def isAnagram(s: str, t: str) -> bool:

    # # Approach 1: b/c both contain same letters sorting should produce same strings
    # return sorted(s) == sorted(t)
    # return Counter(s) == Counter(t)

    # Approach 2: use a dict to store letter counts
    if len(s) != len(t):
        return False
    map_s, map_t = {}, {}

    for a, b in zip(s, t):
        if a not in map_s:
            map_s[a] = 0
        if b not in map_t:
            map_t[b] = 0
        map_s[a] += 1
        map_t[b] += 1
    print(map_s, map_t)
    for k in map_s.keys():
        if (k not in map_t) or (map_s[k] != map_t[k]):
            return False
    return True


s = "a"
t = "ab"
print(isAnagram(s, t))
