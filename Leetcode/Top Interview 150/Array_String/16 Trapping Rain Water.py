def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    n = len(height)
    maxLeft, maxRight, waterLevel = [0] * n, [0] * n, [0] * n

    for i in range(1, n):  # Move left to right after first item
        maxLeft[i] = max(height[i - 1], maxLeft[i - 1])
        j = n - 1 - i  # Move right to left after last item
        maxRight[j] = max(height[j + 1], maxRight[j + 1])
    waterLevel = [min(x, y) for x, y in zip(maxLeft, maxRight)]  #  water  =  min border
    print(waterLevel)
    waterLevel = [
        x - y for x, y in zip(waterLevel, height) if x >= y
    ]  # water = 0 if water<height
    print(waterLevel)

    return sum(waterLevel)


arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(arr))
