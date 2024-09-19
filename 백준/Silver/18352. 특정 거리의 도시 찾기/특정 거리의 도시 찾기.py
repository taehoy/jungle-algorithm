import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N, M, K, X = map(int, input().split())

# [[0], [0], [0], [0], [0]] 만들기
graph = [[0] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)

# 거리 count 리스트 
distance_list = [-1] * (N+1)
distance_list[X] = 0


def bfs(start) :
    q = deque([start])

    while q : 
        cur = q.popleft()
        
        # 연결된 리스트 모두 조회
        for next in graph[cur] :
            if distance_list[next] == -1 : # 
                q.append(next)
                distance_list[next] = distance_list[cur]+1
           


# 출발 도시 X
bfs(X)

if K in distance_list :
    for i in range(1, N+1) :
        if distance_list[i] == K :
            print(i)
else :
    print(-1)