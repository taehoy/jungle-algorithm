import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8) 


N, M = map(int, input().split())
count = 0

graph = [[False] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)

q = []

for i in range(M):
    a, b = map(int, input().split())

    # # bfs에서 처음 시작 큐 설정 
    # if i == 0 :
    #     q.append(a)

    graph[a][b] = True
    graph[b][a] = True

def bfs():
    global q, visited

    while q :
        cur = q.pop()
        visited[cur] = True

        for next in range(1, N+1):
            if not visited[next] and graph[cur][next] :
                visited[next] = True
                q.append(next)

for i in range(1, N+1):
    if not visited[i] :
        count += 1
        q.append(i)
        bfs()

print(count)