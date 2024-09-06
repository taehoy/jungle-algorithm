N = int(input())
list = []
for _ in range(N):
    list.append(int(input()))

list.sort(reverse=False)

for n in list:
    print(n)
