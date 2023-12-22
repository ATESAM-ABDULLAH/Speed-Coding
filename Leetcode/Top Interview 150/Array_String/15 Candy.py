def candy(ratings):
    """
    :type ratings: List[int]
    :rtype: int
    """
    n = len(ratings)

    if n <= 1:  # Only 1 kid
        return n

    # initial state: each kid gets one candy
    nums = [1] * n

    # kids on upwards curve get candies: Going left to right: current > next
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            nums[i] = nums[i - 1] + 1

    # kids on downwards curve get candies: Going right to left: next > current
    # if a kid on both up/down curves, i.e. a peak or a valley
    # kid gets the maximum candies among the two.
    for i in range(n - 1, 0, -1):
        if ratings[i - 1] > ratings[i]:
            nums[i - 1] = max(nums[i] + 1, nums[i - 1])

    return sum(nums)


arr = [1, 3, 4, 5, 2]
print(candy(arr))
