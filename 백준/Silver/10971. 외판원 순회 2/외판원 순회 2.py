import sys

N = int(input())

costs = [list(map(int, input().split())) for _ in range(N)]

min_cost = sys.maxsize

def dfs(cost, visited, cur_idx, start_idx):
    global min_cost

    if all(visited):
        if costs[cur_idx][start_idx] != 0:
            min_cost = min(min_cost, cost+costs[cur_idx][start_idx]) # 출발지로 돌아가는 금액 추가
        return
    
    # 전체 방문이 아닌 경우
    for i in range(N):
        if not visited[i] and costs[cur_idx][i] != 0:
            visited[i] = True
            dfs(cost+costs[cur_idx][i], visited, i, start_idx)
            visited[i] = False


for i in range(N):
    visited = [False] * N
    visited[i] = True
    dfs(0, visited, i, i)

print(min_cost)