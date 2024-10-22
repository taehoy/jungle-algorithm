import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    visited[x][y] = True
    c_color = graph[x][y]

    for next in range(4):
        nx = x + dx[next]
        ny = y + dy[next]
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False :
            if graph[nx][ny] == c_color:    
                dfs(nx,ny)

n = int(input())

graph = [list(input().rstrip()) for _ in range(n)]

visited = [[False] * n for _ in range(n)]

result1, result2 = 0, 0

for i in range(n):
    for j in range(n):
        if visited[i][j] == False :
            dfs(i,j)
            result1 += 1

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == False :
            dfs(i,j)
            result2 += 1

print(result1, result2)

