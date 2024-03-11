def solve():
    n, m, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # print(n, m, k, a, b)
    count=0
    for i in a:
        for j in b:
            if i+j <=k:
                count+=1
    return count


t = int(input())
for i in range(t):
    print(solve())
