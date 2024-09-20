import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**9)

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
needs = [[0] * (n+1) for _ in range(n+1)]

indegree = [0] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[b].append((a,c))
    indegree[a] += 1

def topology_sort():
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0 :
            q.append(i)
    
    while q :
        now = q.popleft()
        
        for next, next_need in graph[now] :
            # 기본 부품인 경우
            if needs[now].count(0) == n+1 :
                needs[next][now] += next_need
            else :
                for i in range(1, n+1):
                    needs[next][i] += needs[now][i] * next_need
            indegree[next] -= 1
            if indegree[next]==0 :
                q.append(next)
            # 기본 부품이 아닌 경우


topology_sort()

for x in enumerate(needs[n]):
    if x[1] > 0 :
        print(*x)