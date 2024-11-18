def solve():
    a, b, c, d = list(map(int, input().split()))
    if a > b:
        a, b = b, a
    if c > d:
        c, d = d, c
    print("ssd  ",a, b, c, d)
    if (c>a and c<b) or (d>a and d<b):
        print("Yes")
    else:
        print("No")


t = int(input())
for _ in range(t):
    solve()
