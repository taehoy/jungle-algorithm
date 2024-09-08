import sys

N = int(sys.stdin.readline())

stack = []

for _ in range(N):
    str = sys.stdin.readline().split()

    cmd = str[0]

    if cmd == "push" : 
        stack.append(int(str[1]))
    elif cmd == "pop" : 
        if len(stack) == 0 :
            print("-1")
        else :
            print(stack.pop())
    elif cmd == "size" :
        print(len(stack))
    elif cmd == "empty" : 
        if len(stack) == 0 :
            print("1")
        else :
            print("0")
    elif cmd == "top" :
        if len(stack) == 0 :
            print("-1")
        else :
            print(stack[-1])