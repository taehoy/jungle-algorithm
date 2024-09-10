import sys
input =  sys.stdin.readline

x, y, w, h = list(map(int,input().split()))

list = []

list.append(x)
list.append(y)
list.append(w-x)
list.append(h-y)

print(min(list))