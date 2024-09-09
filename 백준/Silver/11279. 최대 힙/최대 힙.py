import sys
input = sys.stdin.readline

import heapq

N = int(input())

maxHeap = []

for i in range(N):
    num = int(input()) * -1

    if num == 0 :
        if maxHeap :
            print(heapq.heappop(maxHeap) * -1)
        else :
            print(0)
    else :
        heapq.heappush(maxHeap, num)