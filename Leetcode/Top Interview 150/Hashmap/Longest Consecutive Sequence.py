def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    longest, s = 0, set(nums)
    for num in nums:
        cur_longest = 1  # store longest for 'num'
        streak = 1  # number of consective ints present

        while num - streak in s:  # if  there is a consecutive int < 'num'
            s.remove(num - streak)  # remove it
            cur_longest += 1  # sequence length +1 b/c previous present
            streak += 1  # streak+1 b/c we can continue to next consecutive integer

        streak = 1  # reset  b/c streak broken

        while num + streak in s:  # if  there is a consecutive int > 'num'
            s.remove(num + streak)  # remove it
            cur_longest += 1  # sequence length +1 b/c previous present
            streak += 1  # streak+1 b/c we can continue to next consecutive integer

        longest = max(longest, cur_longest)  # update longest sequence found
    return longest


nums = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(nums))
