import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8) 

# 특정 원소가 속한 집합 찾기
def find_parent(x):
    if parent[x] != x :
        parent[x] = find_parent(parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    parent[b] = a

def same_parent(a, b):
    return find_parent(a) == find_parent(b)

# 노드 개수와 간선 개수 입력받기
v, e = map(int,input().split())
parent = [0] * (v+1) # 부모 테이블 초기화

for i in range(1, v+1):
    parent[i] = i

# 모든 간선을 담을 리스트와, 최종 비용 담을 변수 
edges = []
result = 0

# 모든 간선에 대한 정보 입력받기
for _ in range(e):
    a, b, cost= map(int, input().split())
    
    # 비용순으로 정렬하기 위해 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

# 크루스칼 알고리즘 적용 
# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인
for cost, a, b in edges :
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if not same_parent(a, b):
        union_parent(a, b)
        result += cost

print(result)