import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = []

for _ in range(n):
    coins.append(int(input()))

result = 0
for i in range(n-1, -1, -1):
    if k == 0 :
        break
    #몫과 나눗셈 이용
    #타겟 금액보다 해당 동잔이 크면 pass
    if k < coins[i] :
        continue
    #타겟 금액보다 해당 동전이 작고, 나눌 수 있으면 몫 : 동전 개수 , 나머지 : 남은 타겟 금액

    result += k // coins[i]
    k = k % coins[i]

print(result)
