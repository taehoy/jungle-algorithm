import sys
from collections import deque
input = sys.stdin.readline

v, e = map(int, input().split())

graph = [[] for _ in range(v+1)]
indegree = [0] * (v+1)

# 초기화
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    q = deque()
    result =[]

    for i in range(1, v+1):
        if indegree[i] == 0 :
            q.append(i)

    while q :
        cur = q.popleft()

        result.append(cur)
        
        for next in graph[cur] :
            indegree[next] -= 1
            if indegree[next] == 0 :
                q.append(next)
        
    for i in result :
        print(i, end= " ")

topology_sort()