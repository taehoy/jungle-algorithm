import sys
input = sys.stdin.readline

N = int(input())

count = 0

def findCycle(n):
    global count
    count += 1

    if(count > 1 and n == N):
        return

    tempN = n % 10 + n // 10

    newN = 10*(n % 10) + tempN % 10

    findCycle(newN)

findCycle(N)
print(count-1)
