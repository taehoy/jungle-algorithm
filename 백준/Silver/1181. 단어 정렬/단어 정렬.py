import sys

input = sys.stdin.readline

n = int(input().strip())

lst = []

for i in range(n):
    lst.append(input().strip())

lst = list(set(lst))
lst.sort()
result = sorted(lst, key=len)

for str in result :
    print(str)