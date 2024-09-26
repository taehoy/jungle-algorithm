import sys
from collections import deque
input = sys.stdin.readline

def bfs(y,x):
    count = 1

    q = deque()
    q.append((y,x))

    visited[y][x] = True

    while q:
        y, x = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx] and graph[ny][nx] == 1 :
                visited[ny][nx] = True
                count += 1
                q.append((ny,nx))
    return count

dx = [0,0,1,-1]
dy = [1,-1,0,0]

n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

visited = [[False] * n for _ in range(n)]
# 단지내 집의 수 리스트
result = []

for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == 1 :
            result.append(bfs(i,j))

# 오름차순 정렬
result.sort()

print(len(result))

for i in result :
    print(i)