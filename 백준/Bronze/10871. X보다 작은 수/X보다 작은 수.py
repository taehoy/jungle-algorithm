import sys
input =  sys.stdin.readline

N, X = list(map(int, input().split()))

a = list(map(int, input().split()))

for num in a:
    if num < X : 
        print(num, end=' ')