import sys
# sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())

# 준비물 
board = [list(map(int, input().split())) for _ in range(N)]
whiteCount = 0
blueCount = 0

# 체크함수
def check(startX, startY, endX, endY):
    startColor = board[startX][startY] # 색종이의 처음 색

    for i in range(startX, endX):
        for j in range(startY, endY):
            if not startColor == board[i][j] :
                return 0
    
    if startColor == 1 :
        return 2
    else :
        return 1

# 나누기 함수
def divMap(startX, startY, endX, endY):
    global whiteCount, blueCount

    # 체크했는데 모두 흰색이면 흰색 색종이 +1하고 모두 파란색이면 파란색색종이 +1한다.
    status = check(startX, startY, endX, endY)

    # 만약 같지 않다면 네등분해준다.
    if status == 1 : # 1이면 흰색
        whiteCount += 1
        return
    elif status == 2 : #2면 파란색
        blueCount += 1
        return
    else :
        # 같지 않으니 네등분한다.
        midX = (endX + startX) // 2 
        midY = (endY + startY) // 2

        divMap(startX, startY, midX, midY) # 0,0, 4, 4
        divMap(midX, startY, endX, midY) # 4,0,8,4
        divMap(startX, midY, midX, endY) # 0,4,4,8
        divMap(midX, midY, endX, endY) # 4,4,8,8
    

divMap(0,0,N,N)

print(whiteCount)
print(blueCount)