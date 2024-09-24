import sys
import heapq
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
max_value = float('inf')

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,cost = map(int,input().split())
    graph[a].append((b,cost))

distance = [max_value] * (n+1)

start_point, end_point = map(int, input().split())

def di(start) :
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0

    while q :
        dist, current = heapq.heappop(q)

        if distance[current] < dist :
            continue
        
        for next, next_cost in graph[current] :
            total_cost = dist + next_cost
            if total_cost < distance[next] :
                distance[next] = total_cost
                heapq.heappush(q, (total_cost, next))

di(start_point)

print(distance[end_point])