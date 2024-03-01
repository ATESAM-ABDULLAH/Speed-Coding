def wordPattern(pattern: str, s: str) -> bool:
    mapping = {}
    a = s.split()

    if len(pattern) != len(a):
        return False

    for k, v in zip(pattern, a):
        if k not in mapping:  # new pattern
            if v in mapping.values():  # duplicate word
                return False
            mapping[k] = v  # new pattern -> new word
        if mapping[k] != v:  # existing pattern , different word
            return False
    return True


pattern = "abba"
s = "dog cat cat dog"
print(wordPattern(pattern, s))
