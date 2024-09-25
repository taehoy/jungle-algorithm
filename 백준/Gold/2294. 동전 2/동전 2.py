import sys
input = sys.stdin.readline

n, k = map(int, input().split())

sset = set()
for _ in range(n):
    sset.add(int(input()))

INF = k+1
dp = [INF] * (k+1)
dp[0] = 0

for coin in sset :
    for j in range(1, k+1):
        if 0 <= j-coin :
            dp[j] = min(dp[j], dp[j-coin]+1)

ans = dp[k]

if dp[k] == INF :
    ans = -1
print(ans)