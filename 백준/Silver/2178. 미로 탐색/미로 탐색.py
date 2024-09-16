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
    q = deque()
    q.append((x,y))

    while q :
        x, y = q.popleft() 

        for i in range(4):
            nx = x + dx[i] # 좌우 확인
            ny = y + dy[i] # 상하 확인

            # 그래프 범위 벗어나면 패스
            if nx <0 or nx >=M or ny <0 or ny >= N :
                continue

            # 다음 인접 노드가 0이면 패스
            if graph[ny][nx] == 0 :
                continue

            if graph[ny][nx] ==1 :
                graph[ny][nx] = graph[y][x]+1
                q.append((nx,ny))
            # 다음 인접 노드가 1이면 경로횟수 +1 하고 큐에 넣는다.
    return graph[N-1][M-1]

print(bfs(0,0))