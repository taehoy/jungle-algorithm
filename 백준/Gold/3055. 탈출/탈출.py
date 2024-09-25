from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(input().rstrip()) for _ in range(n)]

visited = [[-1] * m for _ in range(n)]
dy = [-1,1,0,0]
dx = [0,0,-1,1]

q = deque()

for y in range(n):
    for x in range(m):
        if graph[y][x] == '*':
            q.appendleft((y,x))
        elif graph[y][x] == 'S':
            q.append((y,x))
            visited[y][x] = 0

while q :
    y, x = q.popleft()
    cur = graph[y][x]

    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]

        if ny <0 or ny >= n or nx <0 or nx >= m :
            continue
        if visited[ny][nx] != -1 :
            continue
        if graph[ny][nx] == '*':
            continue
        if graph[ny][nx] == 'X' :
            continue
        if cur == '*' and graph[ny][nx] == 'D' :
            continue

        if cur == 'S':
            if graph[ny][nx] == 'D' :
                print(visited[y][x] +1)
                break
            visited[ny][nx] = visited[y][x] + 1
        
        graph[ny][nx] = cur
        q.append((ny,nx))
    else :
        continue
    break
else:
    print("KAKTUS")