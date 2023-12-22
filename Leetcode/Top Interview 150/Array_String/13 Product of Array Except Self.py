import numpy as np


def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    n, ans, suffix_prod = len(nums), [1]*len(nums), 1
    for i in range(1,n):
        ans[i] = ans[i-1] * nums[i-1]
    for i in range(n-1,-1,-1):
        ans[i] *= suffix_prod
        suffix_prod *= nums[i]
    return ans


arr = [1, 2, 3, 4]
print(productExceptSelf(arr))
