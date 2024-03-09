def insert(intervals, newInterval):
    """
    :type intervals: List[List[int]] -> sorted ascending
    :type newInterval: List[int]
    :rtype: List[List[int]]
    """
    left, right = [], []
    for i in intervals:
        if i[1] < newInterval[0]:  # smaller interval
            left.append(i)
        elif i[0] > newInterval[1]:  #  larger interval
            right.append(i)
        else:  # merge
            newInterval = [min(newInterval[0], i[0]), max(newInterval[1], i[1])]
    return left + [newInterval] + right


intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]
print(insert(intervals, newInterval))
