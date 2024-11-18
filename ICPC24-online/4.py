def max_energy(energy):
    n, m = len(energy), len(energy[0])
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = energy[0][0]

    for j in range(1, m):
        dp[0][j] = dp[0][j - 1] + energy[0][j]

    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + energy[i][0]

    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + energy[i][j]

    return dp[n - 1][m - 1]


def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        energy = []
        for _ in range(n):
            energy.append(list(map(int, input().split())))
        print(max_energy(energy))


if __name__ == "__main__":
    main()
