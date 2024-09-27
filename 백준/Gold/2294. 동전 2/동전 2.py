import sys
input = sys.stdin.readline
INF = sys.maxsize

n, k = map(int, input().split())

dp = [INF] * (k+1)
dp[0] = 0

coins = set()

for _ in range(n):
    coins.add(int(input()))


for coin in coins :
    for i in range(1, k+1):
        if 0 <= i-coin :
            dp[i] = min(dp[i], dp[i-coin]+1)

ans = dp[k]
#최소 비용 출력

if dp[k] == INF :
    ans = -1

print(ans)

#     # 나누어 떨어질때
