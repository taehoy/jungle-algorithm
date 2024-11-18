import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, height):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        cx, cy = q.popleft()

        for next in range(4):
            nx = cx + dx[next]
            ny = cy + dy[next]

            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > height and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))


n = int(input())

max_num = 0
graph = []

for _ in range(n):
    low = list(map(int, input().split()))
    graph.append(low)

    max_num = max(max_num, max(low))

answer = 0

for i in range(max_num):
    count = 0
    visited = [[False] * n for _ in range(n)]

    for j in range(n):
        for k in range(n):
            if not visited[j][k] and graph[j][k] > i :
                bfs(j,k,i)
                count += 1
    
    answer = max(count, answer)

print(answer)