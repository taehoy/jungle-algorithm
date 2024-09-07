import sys

n = int(sys.stdin.readline().strip())

arr = []

for _ in range(n):
    arr.append(sys.stdin.readline().strip())

set_arr = set(arr)
arr = list(set_arr)
arr.sort()
arr.sort(key=len)

for str in arr:
    print(str)