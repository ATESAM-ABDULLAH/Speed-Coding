import numpy as np


def jump(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # jmp = p + nums[p] i.e index + nums[index]
    # use argmax to find highest jump possible from current loc
    p = 0
    s = 0 if len(nums) == 1 else 1
    jmp = [i + x for i, x in enumerate(nums)]
    print(jmp)
    while (p + nums[p]) < (len(nums) - 1):
        s += 1
        p += 1 + np.argmax(jmp[p + 1 : p + nums[p] + 1])
    return s


arr = [1, 2, 1, 1, 1]
print(jump(arr))
# print(np.argmax(arr[0+1:2+1]),arr[0+1:2+1])
