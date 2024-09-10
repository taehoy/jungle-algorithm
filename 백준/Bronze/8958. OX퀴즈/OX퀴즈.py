import sys
input =  sys.stdin.readline

N = int(input())
count = 0
for i in range(N):
    word = input()
    score = 0
    
    for s in word :
        if s == 'O' :
            count += 1
            score += count
        else :
            count = 0
    print(score)