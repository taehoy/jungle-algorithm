import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**8)

N = int(input())
M = int(input())

graph = [[False] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

count = 0
def dfs(idx):
    global visited, count

    visited[idx] = True
    
    for next in range(1, N+1):
        if not visited[next] and graph[idx][next] :
            count +=1 # 방문하지 않고 연결되었을 경우, 컴퓨터가 감염되었으므로 count+1
            dfs(next)

dfs(1)
print(count)