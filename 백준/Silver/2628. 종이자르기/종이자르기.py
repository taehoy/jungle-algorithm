import sys
import math
input =  sys.stdin.readline

width, height = map(int,input().split())

lstX = [0]
lstY = [0]

N = int(input())

for _ in range(N):
    a, b = list(map(int,input().split()))

    if a == 0 :
        lstX.append(b)
    else :
        lstY.append(b)

lstX.append(height)
lstY.append(width)

maxX = 0
maxY = 0

lstX.sort()
lstY.sort()

for i in range(len(lstX) -1):
    diff1 = lstX[i+1] - lstX[i]
    maxX = max(maxX, diff1)

for i in range(len(lstY) -1):
    diff = lstY[i+1] - lstY[i]
    maxY = max(maxY, diff)

print(maxX * maxY)