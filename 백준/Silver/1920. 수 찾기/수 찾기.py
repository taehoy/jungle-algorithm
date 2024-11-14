import sys
input = sys.stdin.readline

n = int(input())
arr = set(map(int, input().split()))

m = int(input())
nums = list(map(int, input().split()))

for num in nums :
    print(1) if num in arr else print(0)