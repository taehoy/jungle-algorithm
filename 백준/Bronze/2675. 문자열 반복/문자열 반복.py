T = int(input())

for i in range(T) :
    cmd = input().split()
    n = int(cmd[0])
    str = cmd[1]
    
    result = ""
    for j in range(0, len(str)):
        result += str[j] *n
        
    print(result)
