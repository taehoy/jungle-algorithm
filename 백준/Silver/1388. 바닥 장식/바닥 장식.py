import sys

input = sys.stdin.readline

def dfs(y,x):
    if graph[y][x] == '-':
        graph[y][x] = -1
        # 좌우
        for next in [1,-1]:
            nx = x + next
            if 0<=nx<m and graph[y][nx] == '-':
                dfs(y,nx)
    if graph[y][x] == '|':
        graph[y][x] = -1

        for next in [1,-1]:
            ny = y + next
            if 0 <= ny < n and graph[ny][x] == '|':
                dfs(ny,x)

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(input().rstrip()))

#나무 판자 개수
result = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == '-' or graph[i][j] == '|':
            dfs(i,j)
            result += 1

print(result)