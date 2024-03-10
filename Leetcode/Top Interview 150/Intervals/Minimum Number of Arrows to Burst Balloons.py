def findMinArrowShots(points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    points.sort(key=lambda x: x[1])
    print(points)
    arrows, j = 1, 0
    for i in range(1, len(points)):
        print(points[j][1], points[i][0])
        if points[j][1] < points[i][0]:  # new range
            arrows += 1
            j = i
        print(i,j,arrows)
    return arrows


points = [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]
print(findMinArrowShots(points))
