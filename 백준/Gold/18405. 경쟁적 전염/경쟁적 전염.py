import sys
import heapq
input = sys.stdin.readline

#, 매 초마다 번호가 낮은 종류의 바이러스부터 먼저 증식한다. 
# 증식 과정에서 특정한 칸에 이미 어떠한 바이러스가 존재한다면, 그 곳에는 다른 바이러스가 들어갈 수 없다.

dx = [0,0,1,-1]
dy = [1,-1,0,0]

n , m = map(int,input().split())

graph = [[0] * (n+1) for _ in range(n+1)]

virus = []

for i in range(1, n+1):
    temp = list(map(int,input().split()))
    for j in range(1, n+1):
        graph[i][j] = temp[j-1]
        if graph[i][j] != 0 :
            heapq.heappush(virus, (graph[i][j], i,j))

visited = [[False]* (n+1) for _ in range(n+1)]

limit, virus_x, virus_y = map(int,input().split())

count = 0 # 0초 지남

for i in range(limit):
    temp = []

    while virus :
        virus_num, y, x = heapq.heappop(virus)
        visited[y][x] = True    

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0< ny < n+1 and 0 < nx < n+1 and graph[ny][nx] == 0 and not visited[ny][nx]:
                graph[ny][nx] = virus_num
                visited[ny][nx] = True
                temp.append((graph[ny][nx], ny, nx)) # 연결된 바이러스의 정보를 다시 리스트에 넣는다.

    for v in temp :
        heapq.heappush(virus, v)

print(graph[virus_x][virus_y])
