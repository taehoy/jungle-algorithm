a = []
for i in range(9):
    a.append(int(input()))

max = max(a)

print(max)
print(a.index(max)+1)