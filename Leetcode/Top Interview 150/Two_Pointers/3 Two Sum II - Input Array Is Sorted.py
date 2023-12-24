def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    # x+y : x<y = target
    # l<r : x = num[l], y = num[r]
    # numbers is sorted ascending
    l = 0
    r = len(numbers) - 1
    while numbers[l] + numbers[r] != target:
        if numbers[l] + numbers[r] < target:  # if sum<target: l is too small
            l += 1
        else:  # if sum>target: r is too big
            r -= 1
    return l + 1, r + 1



numbers = [0, 0, 3, 4]
target = 0
print(twoSum(numbers, target))
