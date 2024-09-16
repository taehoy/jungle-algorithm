import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**8) 

# 상하좌우 확인시 필요한 리스트
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0] 

N, M = map(int, input().split())

graph = []

for i in range(N):
    graph.append(list(map(int, input().rstrip())))

def bfs(x, y):
    q = deque([(x,y)]) # 큐 초기화시 값 넣기(리스트)

    while q :
        x, y = q.popleft() 

        for i in range(4):
            nx = x + dx[i] # 좌우 확인
            ny = y + dy[i] # 상하 확인

            # 그래프 범위 벗어나면 패스
            if 0 <= nx < M and 0 <= ny < N and graph[ny][nx] ==1 :
                graph[ny][nx] = graph[y][x]+1
                q.append((nx,ny))

    return graph[N-1][M-1]

print(bfs(0,0))