import sys
input = sys.stdin.readline

t = int(input())

result = []

for _ in range(t):

    n = int(input())
    coins = list(map(int, input().split()))
    coins.insert(0,0)
    m = int(input())

    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(n+1):
        dp[i][0] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = dp[i-1][j]

            if j-coins[i] >= 0:
                dp[i][j] += dp[i][j-coins[i]]
    result.append(dp[n][m])

for i in result :
    print(i)
