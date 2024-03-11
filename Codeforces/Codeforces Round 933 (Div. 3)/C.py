def solve():
    n = int(input())
    s = input()
    return s.count("map") + s.count("pie")


t = int(input())
for i in range(t):
    print(solve())
