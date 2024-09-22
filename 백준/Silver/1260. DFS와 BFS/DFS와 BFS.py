# https://www.acmicpc.net/problem/2606
# 바이러스
# 시간복잡도 : O(n^2)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
from collections import deque

n, m, first = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
result = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

def dfs(first):
    stack = []
    stack.append(first)
    visited[first] = True

    while stack :
        now = stack.pop()

        if result.count(now) == 0 :
            result.append(now)
        
        visited[now] = True

        for next in graph[now][::-1]:
            if not visited[next]:
                stack.append(next)

    print(*result)

def bfs(first):
    q = deque()
    q.append(first)

    visited[first] = True

    while q :
        now = q.popleft()
        print(now, end=' ')
        for next in graph[now]:
            if not visited[next] :
                visited[next] = True
                q.append(next)
                

dfs(first)

visited = [False]*(n+1)

bfs(first)
