def solve():
    n = int(input())
    a = list(map(int, input().split()))
    i = a.index(max(a))
    while (i > 0) and (i < n - 1):
        a[i - 1] -= 1
        a[i] -= 2
        a[i + 1] -= 1
        # print(i, a)
        i = a.index(max(a))
        if all([x == 0 for x in a]):
            return "YES"
    return "NO"


t = int(input())
for i in range(t):
    print(solve())
