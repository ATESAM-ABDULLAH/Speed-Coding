from random import sample

def solve():
    s = input()
    x = set(s)
    if len(x) > 1:
        print("Yes")
        r = "".join(sample(s, len(s)))
        while r==s:
            r = "".join(sample(s, len(s)))
        print(r)
    else:
        print("No")


t = int(input())
for _ in range(t):
    solve()
