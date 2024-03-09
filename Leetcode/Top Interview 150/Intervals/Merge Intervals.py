def merge(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    res = []
    intervals.sort(key=lambda x: x[0])  # sort
    for i in range(len(intervals)):
        if (not res) or intervals[i][0] > res[-1][1]:  # new interval
            res.append(intervals[i])
        else:  # old interval
            res[-1][0] = min(intervals[i][0], res[-1][0])
            res[-1][1] = max(intervals[i][1], res[-1][1])
    return res


intervals = [[1, 9], [0, 5]]  # [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge(intervals))
