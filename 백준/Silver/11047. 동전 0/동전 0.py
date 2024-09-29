import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = []

for _ in range(n):
    coins.append(int(input()))

result = 0
for i in range(n-1, -1, -1):
    coin = coins[i]
    while True :
        if coin > k :
            break

        k -= coin
        result += 1

print(result)
