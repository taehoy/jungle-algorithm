import sys
input = sys.stdin.readline

import heapq

N = int(input())

maxHeap = []

for i in range(N):
    num = int(input()) * -1

    if num == 0 :
        print(heapq.heappop(maxHeap) * -1 if maxHeap else 0)
    else :
        heapq.heappush(maxHeap, num)