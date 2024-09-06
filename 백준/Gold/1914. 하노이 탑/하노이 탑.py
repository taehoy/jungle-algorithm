def hanoiTop(n, a, b, c):
    if n == 1:
        print(a, c)
        return
    
    hanoiTop(n-1,a, c, b)
    hanoiTop(1, a, b, c)
    hanoiTop(n-1, b, a, c)

N = int(input())

print(2**N-1)

if(N<=20):
    hanoiTop(N,1,2,3)
