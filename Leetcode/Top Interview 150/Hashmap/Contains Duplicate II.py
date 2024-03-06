def containsNearbyDuplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    mem = {}
    for i, x in enumerate(nums):
        # print(mem)
        if (x in mem) and (abs(mem[x] - i) <= k):
            return True
        mem[x] = i
    return False


nums = [1, 0, 1, 1]
k = 1
print(containsNearbyDuplicate(nums, k))
