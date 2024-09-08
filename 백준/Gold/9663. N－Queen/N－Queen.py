N = int(input())

board = [0 for _ in range(N)]

count = 0

# 퀸 위치 가능 여부 함수
def checkPlace(y):
    for i in range(y):
        if (board[y] == board[i] or abs(board[y] - board[i]) == abs(y-i)):
            return False
    return True

# 퀸 위치에 두기 함수
def placeQueen(y):
    global count

    if y == N :
        count += 1
    else:
        for i in range(N):
            board[y] = i # 퀸을 놓는다.
            if(checkPlace(y)): # 퀸의 위치를 체크한다. (가로, 세로, 대각선 X)
                placeQueen(y+1)
            board[y] = 0

placeQueen(0)
print(count)
