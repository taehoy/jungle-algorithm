N = int(input())
a = list(map(int, input().split()))
a.sort()

M = int(input())
b = list(map(int, input().split()))

def binarySearch(target):
    st = 0
    en = len(a)-1
    while(st <= en):
        mid = (st+en) // 2
        if a[mid] > target :
            en = mid-1
        elif a[mid] < target :
            st = mid+1
        else :
            return 1    
    return 0

for i in b:
    print(binarySearch(i))
