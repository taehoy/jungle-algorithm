import sys
from collections import deque

cmd = list(map(int, input().split()))

N = cmd[0]
K = cmd[1]

queue = deque()
ans = []
count = 0

for i in range(1, N+1):
    queue.append(i)

while queue :
    if count == K-1:
        ans.append(queue.popleft())
        count = 0
    else :
        queue.append(queue.popleft())
        count += 1

result = "<"

for i in range(len(ans)-1) :
    result += str(ans[i]) +", "

result += str(ans[-1]) + ">"

print(result)