def min_energy(p):
    n = len(p) - 1
    dp = [[0] * n for _ in range(n)]

    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            dp[i][j] = float("inf")
            for k in range(i, j):
                dp[i][j] = min(
                    dp[i][j], dp[i][k] + dp[k + 1][j] + p[i - 1] * p[k] * p[j]
                )

    return dp[0][n - 1]


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        p = list(map(int, input().split()))
        print(min_energy(p))


if __name__ == "__main__":
    main()
