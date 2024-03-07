def summaryRanges(nums):
    """
    :type nums: List[int]
    :rtype: List[str]
    """
    ranges = []
    for i, x in enumerate(nums):
        if ranges and ranges[-1][1] == x - 1:  # check if last range ends on x-1
            ranges[-1][1] = x  # update range b/c x is present
        else:
            ranges.append([x, x])  # new range found
        # print(i, x, ranges)
    ranges = [str(a) + "->" + str(b) if a != b else str(a) for a, b in ranges]
    return ranges


nums = [0, 1, 2, 4, 5, 7]
print(summaryRanges(nums))
