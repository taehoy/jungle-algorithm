import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

arr = []

while True :
    try:
        arr.append(int(input()))
    except :
        break

def post_order_to_reverse(arr):
    # 배열의 길이가0이면 return
    if len(arr) == 0 :
        return
    # 왼쪽트리, 오른쪽 트리 리스트 생성
    left, right =[], []
    # 루트값 설정
    root = arr[0]

    # 리스트를 돌면서 루트값보다 클경우 그 전까지의 값을 왼쪽트리에, 그 이후 값을 오른쪽 트리에 넣고 재귀함수 호출
    for i in range(1, len(arr)):
        if arr[i] > root :
            left = arr[1:i]
            right = arr[i:]
            break
    # 루트값보다 큰게 없다면 왼쪽 노드
    else :
        left = arr[1:]

    # 후위순회니까 왼오값
    post_order_to_reverse(left)
    post_order_to_reverse(right)
    print(root)

post_order_to_reverse(arr)
