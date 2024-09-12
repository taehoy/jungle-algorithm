import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

arr = []

while True :
    try:
        x = int(input())
        arr.append(x)
    except ValueError :
        break

def post_order_traversal(A):
    # 길이가 0 이면 리턴
    if len(A)==0:
        return
    
    # 첫번째 값이 루트값
    tempL, tempR = [], []
    root = A[0]

    # 인덱스 1부터 len(a)-1까지 순회
    for i in range(1, len(A)):
        if A[i] > root :
            tempR = A[i:]
            tempL = A[1:i]
            break
    else :
        tempR = A[1:]
        # 루트보다 A[i]가 크면 1~ i-1은 왼쪽노드에, i ~ 는 오른쪽 노드
        # A[i]가 작으면 모두 오른쪽 노드
    
    # 후위순회니까 왼오값 
    post_order_traversal(tempL)
    post_order_traversal(tempR)
    print(root)

post_order_traversal(arr)