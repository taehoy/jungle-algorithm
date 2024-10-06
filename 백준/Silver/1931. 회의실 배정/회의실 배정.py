import sys
import heapq
input = sys.stdin.readline

end_time = 0
n = int(input())

lect = []
count=0

for _ in range(n):
    lect.append(list(map(int,input().split())))

lect.sort(key=lambda x: (x[1],x[0]))

for start, end in lect:
    if end_time <=start :
        count+=1
        end_time = end

print(count)