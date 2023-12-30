def minSubArrayLen(target, nums):
    """
    :type target: int
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    l, cur_sum, min_len = (
        0,
        0,
        n + 1,
    )  # left pointer, sum of subarray, min sub array length

    for r in range(n):
        cur_sum += nums[r]  # add right item to list
        r += 1  # move right pointer right
        while cur_sum >= target:  # valid subarray found -> optimize it
            cur_sum -= nums[l]  # remove the left item
            min_len = min(min_len, r - l)  # if smaller subarray found
            l += 1  # move left pointer right
    return min_len if min_len <= n else 0


target = 2
nums = [1, 4, 4]

print(minSubArrayLen(target, nums))
