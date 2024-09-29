import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dp = [0] * (k+1)
dp[0] = 0
bags = []

for i in range(n):
    a, b = map(int,input().split())
    bags.append((a,b))

bags.sort()

for bag in bags :
    for i in range(k,bag[0]-1,-1):
        dp[i] = max(dp[i-bag[0]] + bag[1], dp[i])

print(dp[k])


