import sys
from collections import deque
input = sys.stdin.readline

sys.setrecursionlimit(10**8)

K = int(input())

def bfs(start) :
    q = deque([start])
    visited[start] = 1

    while q :
        cur = q.popleft()

        for next in graph[cur] :
            if not visited[next] :
                q.append(next)
                visited[next] = -visited[cur]
            elif visited[next] == visited[cur]:
                return False
    return True
    

for _ in range(K):

    N, M = map(int, input().split())

    graph = [[] for _ in range(N+1)]

    visited = [False] * (N+1)

    for i in range(M) :
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    for i in range(N+1):
        if not visited[i] :
            result = bfs(i)
            if not result :
                break
    
    if result :
        print("YES")
    else :
        print("NO")