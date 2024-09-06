# 소수만드는 함수
# True면 소수, False면 소수 X 
def isPrime(num):
    if num ==1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False 
    
    return True

T = int(input())
arr = list(map(int,input().split()))

result = 0
for n in arr :
    if isPrime(n) :
        result += 1
    
print(result)
