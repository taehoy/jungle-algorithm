import sys
input = sys.stdin.readline

t = int(input()) 

arr = [0, 1, 2, 4]

for _ in range(t):
    n = int(input())
    
    if n < 4 :
        print(arr[n])
        continue

    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4,n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[n])