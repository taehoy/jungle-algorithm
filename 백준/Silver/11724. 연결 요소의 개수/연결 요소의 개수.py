import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8) 


N, M = map(int, input().split())
count = 0

graph = [[False] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

def dfs(idx):
    global visited

    visited[idx] = True

    for next in range(1, N+1):
        if not visited[next] and graph[idx][next] :
            dfs(next)

for i in range(1, N+1):
    if visited[i] == False:
        count +=1
        dfs(i)

print(count)