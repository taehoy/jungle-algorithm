import sys
input = sys.stdin.readline

def dfs():
    global count, sum
    if sum > n : 
        return

    if sum == n :
        count+=1
        return
    
    for i in range(1,4):
        sum += i
        dfs()
        sum -= i

t = int(input())

for _ in range(t):
    n = int(input())

    count = 0
    sum = 0

    dfs()
    print(count)
