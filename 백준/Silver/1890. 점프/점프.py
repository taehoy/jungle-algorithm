import sys
input = sys.stdin.readline

# 2차원 dp
# dfs + dp

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

# 방문처리 : dp의 값이 -1이 아니면 방문한것
dp = [[0] * n for _ in range(n)]

dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if dp[i][j] == 0 or (i == n-1 and j == n-1) :
            continue
        if i + graph[i][j] < n :
            dp[i+graph[i][j]][j] += dp[i][j]
        if j + graph[i][j] < n :
            dp[i][j + graph[i][j]] += dp[i][j]

print(dp[n-1][n-1])