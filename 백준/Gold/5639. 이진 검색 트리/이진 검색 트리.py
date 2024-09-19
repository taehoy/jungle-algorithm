import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

arr = []

while True :
    try :
        arr.append(int(input()))
    except :
        break

def post_order_to_reverse(A):
    # 길이가 0인 경우 리턴
    if len(A) == 0 :
        return
    # 왼쪽 오른쪽 리스트 생성
    tempL, tempR = [], []
    # 루트값 정의
    root = A[0]

    # 루트값과 비교하여 큰경우 자르기 시전
    for i in range(1, len(A)):
        if A[i] > root :
            tempL = A[1:i]
            tempR = A[i:]
            break
    else :
        tempR = A[1:]

    post_order_to_reverse(tempL)
    post_order_to_reverse(tempR)
    print(root)
        

post_order_to_reverse(arr)