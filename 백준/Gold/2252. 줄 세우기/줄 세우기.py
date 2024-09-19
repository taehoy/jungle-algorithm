import sys
input = sys.stdin.readline
from collections import deque

# v : 노드 개수
# e : 간선 개수
v, e = map(int, input().split())

# 모든 노드에 대한 진입차수 0 초기화
indegree = [0] * (v+1)

# 각 노드에 연결된 간선 정보 담기 위한 연결 리스트 초기화
graph = [[] for _ in range(v+1)]

# 방향 그래프의 모든 간선 정보 입력 받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    # 진입 차수 증가
    indegree[b] += 1

def topology_sort():
    # 알고리즘 수행 결과 담을 리스트
    result = []

    # 큐 선언
    q = deque()
    # 처음 시작 시 진입차수 0인 노드 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0 :
            q.append(i)

    # 큐가 빌 떄까지 반복
    while q :
        # 큐에서 원소 꺼내기
        cur = q.popleft()
        result.append(cur)

        # 해당 원소와 인접 노드들의 진입차수에서 1 빼기
        for next in graph[cur] :
            indegree[next] -= 1
            # 진입차수가 0이 되는 새로운 노드들을 큐에 삽입
            if indegree[next] == 0 :
                q.append(next)

    # 위상 정렬 수행 결과 출력
    for i in result :
        print(i, end=" ")
topology_sort()
