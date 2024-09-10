import sys
input =  sys.stdin.readline

result= int(input()) * int(input()) * int(input())

s = str(result)

arr = [0]*10

for st in s :
    arr[int(st)] += 1


for n in arr :
    print(n)