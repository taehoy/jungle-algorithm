import sys
input = sys.stdin.readline

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

whileCount = 0 
blueCount = 0

def checkColor(startX, startY, endX, endY):

    startColor = board[startX][startY]

    for i in range(startX, endX):
        for j in range(startY, endY):
            if not board[i][j] == startColor :
                return 0
    
    if startColor == 0 :
        return 1 # 흰색인 경우 1
    else :
        return 2 # 파란색인 경우 2

def sepBoard(startX, startY, endX, endY):
    global whileCount, blueCount

    status = checkColor(startX, startY, endX, endY) 

    if status == 1 :
        whileCount += 1
        return
    elif status == 2 :
        blueCount += 1
        return
    else :
        midX = (startX + endX) // 2
        midY = (startY + endY) // 2

        sepBoard(startX, startY,midX,midY)
        sepBoard(midX, startY,endX,midY)
        sepBoard(startX, midY,midX,endY)
        sepBoard(midX, midY,endX,endY)

sepBoard(0,0,N,N)
print(whileCount)
print(blueCount)