import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**8)

N = int(input())

graph = [[] * (N+1) for _ in range(N+1)]

# 노드 별 부모 리스트  ex) 2번노드 -> result[2]
result = [0] * (N+1)

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a) 

def dfs(idx):

    for next in graph[idx]:
        if result[next] == 0 :
            result[next] = idx # 부모에서 자식을 호출 할 때, 부모 리스트에 추가
            dfs(next)

dfs(1)
for x in range(2, N+1):
    print(result[x])