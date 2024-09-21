import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
from collections import deque

n = int(input())

s = input().rstrip()
inout = [-1]
for i in range(len(s)):
    inout.append(int(s[i]))

graph = [[] for _ in range(n+1)]

count = 0

while True :
    try :
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        if inout[a] == 1 and inout[b] == 1 :
            count += 2
    except :
        break

def bfs(first):
    global count
    n = 0 # 1의 개수 => 순열을 위함 

    q = deque([first])
    visited[first] = True    
    
    while q :
        now = q.popleft()

        for next in graph[now]:
            # 0에서 1로 가는것 : 줄 수 세고 큐에 넣지는 말기
            if inout[next] == 1 :
                n += 1
            # 0에서 0으로 가는 것 : 줄 수 세지 말고 큐에 넣기
            elif inout[next] == 0 :
                if not visited[next] :
                    visited[next] = True
                    q.append(next)
    #순열 계산
    count += n * (n-1)

visited = [False] * (n+1)
for i in range(1, n+1):
    if inout[i] == 0 :
        if not visited[i] :
            bfs(i)

print(count)