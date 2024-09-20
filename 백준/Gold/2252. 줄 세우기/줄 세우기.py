import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def bfs():
    q = deque()
    result = []
    for i in range(1, n+1):
        if indegree[i] == 0 :
            q.append(i)

    while q :
        now = q.popleft()
        result.append(now)

        for next in graph[now]:
            indegree[next] -= 1
            if indegree[next] == 0 :
                q.append(next)
    
    print(*result)

bfs()