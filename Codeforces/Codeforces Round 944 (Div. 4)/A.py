def solve():
    x, y = list(map(int, input().split()))
    if x < y:
        return x, y
    else:
        return y, x


t = int(input())
for _ in range(t):
    x,y = solve()
    print(x,y)