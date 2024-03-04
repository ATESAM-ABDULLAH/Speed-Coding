def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    # Create a dictionary to store sorted words
    word_dict = {}
    for w in strs:
        a = "".join(sorted(w))
        # print(w, a)
        if a not in word_dict:
            word_dict[a] = [w]
        else:
            word_dict[a].append(w)
    return list(word_dict.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
