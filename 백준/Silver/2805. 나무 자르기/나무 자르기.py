import sys
input = sys.stdin.readline

# N: 나무의 수, target: 가져가려는 나무의 길이
N, target = map(int, input().split())
trees = list(map(int, input().split()))

# 나무 자르기 함수: mid 높이로 자를 때 얻을 수 있는 나무 길이
def sliceTree(mid):
    cur = 0
    for tree in trees:
        if tree > mid:
            cur += tree - mid
    return cur

# 이진 탐색 시작
start, end = 0, max(trees)
result = 0

while start <= end:
    mid = (start + end) // 2
    count = sliceTree(mid)
    
    if count >= target:  # 목표 나무 길이보다 크거나 같을 때
        result = mid  # 일단 가능한 높이로 저장
        start = mid + 1  # 더 높은 높이로 시도
    else:
        end = mid - 1  # 나무 길이가 부족하면 낮은 높이로 시도

print(result)
