import sys
input = sys.stdin.readline

n = int(input())

stack = []
result = [0] * n
towers = list(map(int, input().split()))

for i in range(n) :
    while stack :
        if stack[-1][1] > towers[i] :
            result[i] = stack[-1][0]
            break
        else :
            stack.pop()

    stack.append((i+1, towers[i]))

print(*result)