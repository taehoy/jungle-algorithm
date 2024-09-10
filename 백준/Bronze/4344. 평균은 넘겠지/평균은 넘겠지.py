import sys
input =  sys.stdin.readline

N = int(input())

for _ in range(N):
    arr = list(map(int,input().split()))

    #학생 수
    num = arr[0]
    
    arr.remove(arr[0])

    total = sum(arr)

    avg = total // len(arr)

    count = 0 

    for score in arr :
        if score > avg :
            count +=1
    
    # 평균 넘는 비율 : count / len(arr)
    balance = count / len(arr)* 100

    print("{:.3f}".format(balance)+"%")