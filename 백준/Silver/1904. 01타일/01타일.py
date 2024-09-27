import sys
input = sys.stdin.readline

n = int(input())

arr = [1,2]

for i in range(2, n):
    num = (arr[i-1]+arr[i-2]) % 15746
    
    arr.append(num)
    
print(arr[n-1])
