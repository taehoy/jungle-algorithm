import sys
import heapq
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
INF = float('inf') # 무한 의미로 10억 설정

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append((b,1))

distances = [INF] * (N+1)

def di(start):
    q = []
    heapq.heappush(q, (0,start))
    distances[start] = 0
    
    while q : 
        dist, now = heapq.heappop(q)
        
        if distances[now] < dist :
            continue
        
        for next, next_cost in graph[now]:
            total_cost = dist + next_cost

            if total_cost < distances[next] :
                distances[next] = total_cost
                heapq.heappush(q, (total_cost, next))
    
di(X)
flag = False
for i in range(1, N+1):
    if distances[i] == K :
        flag = True
        print(i)

if not flag :
    print(-1)