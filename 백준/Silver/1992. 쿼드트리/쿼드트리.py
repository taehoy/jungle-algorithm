import sys
input = sys.stdin.readline

result = "("
N = int(input())

board = []

for i in range(N):
    str = list(input().rstrip('\n'))
    board.append(str)

result = ''

def checkZeroOrOne(board, startY, startX, endY, endX):

    # 처음 숫자
    status = board[startY][startX]

    for i in range(startY, endY):
        for j in range(startX, endX):
            if board[i][j] != status :
                return 2
    
    # 0으로 꽉 채워져있을때
    if status == '0' : 
        return 0
    elif status == '1' : # 1로 꽉 채워져있을때
        return 1
    

def divBoard(board, startY, startX, endY, endX):

    global result

    status = checkZeroOrOne(board, startY, startX,endY, endX)

    if status == 0 :
        result += "0"
    elif status == 1 :
        result += "1"
    else :
        midX = (startX + endX) // 2
        midY = (startY + endY) // 2
        result += "("
        divBoard(board, startY, startX, midY, midX)
        divBoard(board, startY, midX, midY, endX)
        divBoard(board, midY, startX, endY, midX)
        divBoard(board, midY, midX, endY, endX)
        result += ")"

divBoard(board, 0, 0, N, N)
print(result)