import sys
input = sys.stdin.readline

def isPrime(num):
    if num == 1 :
        return False
    
    for i in range(2, int(num**0.5)+1):
        if num % i == 0 :
            return False
    return True

T = int(input())

for _ in range(T) :
    num = int(input())

    a, b = num//2, num//2

    while a>0 :
        if isPrime(a) and isPrime(b) :
            print(a, b)
            break
        else:
            a -= 1
            b += 1