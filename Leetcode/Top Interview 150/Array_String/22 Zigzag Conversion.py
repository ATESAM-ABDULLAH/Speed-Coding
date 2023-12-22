def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows == 1 or numRows >= len(s):  # No zig zag possible
        return s
    # The patterns goes from from 0->(rows-1)->0->(rows-1)->0
    # Thus  if index = 0, we increase it
    #       if index = rows-1, we decrease it
    L = [""] * numRows  # string in each row
    index, step = 0, 1  # current row index, increase/decrease index

    for x in s:
        L[index] += x  # add letter to row index
        # print(L)
        if index == 0:  # if index low
            step = 1  # increase index
        elif index == numRows - 1:  # if index highest
            step = -1  # decrease index
        index += step

    return "".join(L)


s = "PAYPALISHIRING"
r = 4
print(convert(s, r))
