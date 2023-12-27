def maxArea(height):
    """
    :type height: List[int]
    :rtype: int"""
    # left ptr, right ptr, max height in all list (best ans)
    l, r, max_height = 0, len(height) - 1, max(height)
    # water in container (left,right)
    water = 0

    while l < r:  # Loop until both pointers meet
        # max water stored = Max(old_water,new_water)
        water = max(water, min(height[l], height[r]) * (r - l))
        if height[l] < height[r]:  # if left bar is limiting factor
            l += 1
        else:  # if right bar is limiting factor
            r -= 1

        if (max_height * (r - l)) <= water:  # if optimum solution reached
            break  # break early

    return water


h = [1, 2, 4, 3]

print(maxArea(h))
