def hIndex(citations):
    """
    :type citations: List[int]
    :rtype: int
    """
    # 1st approach
    citations.sort(reverse=True)  # sort citations descending
    h = 0
    for ind, cit in enumerate(citations):
        if cit >= ind + 1:  # if citations >= num papers with that many citations
            h += 1
    return h


## 2nd approach
# or  return sum(i < j for i, j in enumerate(sorted(citations, reverse=True)))


print(hIndex([3, 5, 6, 0, 1]))
