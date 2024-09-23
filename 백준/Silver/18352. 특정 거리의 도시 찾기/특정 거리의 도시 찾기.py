import sys
import heapq
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
from collections import deque
INF = int(1e9) # 무한 의미로 10억 설정

n, m, k, x = map(int,input().split())

graph = [[] for i in range(n+1)]

distance = [INF] * (n+1)

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append((b,1))

def dijkstra(start) :
    q = []

    # 힙 저장 방식 (거리, 노드)
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist :
            continue
        
        for next, next_cost in graph[now]:
            cost = dist+next_cost

            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q, (cost, next))


dijkstra(x)
flag = False
for i in range(1, n+1):
    if distance[i] == k :
        flag = True
        print(i)

if not flag :
    print(-1)