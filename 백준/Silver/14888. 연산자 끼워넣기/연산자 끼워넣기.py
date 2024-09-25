import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())

nums = list(map(int, input().split()))
arr = list(map(int, input().split()))

min_value = sys.maxsize
max_value = -sys.maxsize

def dfs(arr, result, idx):
    global n, min_value, max_value

    # 계산한 횟수가 n번이면 값 비교하고 리턴시킴
    if n == idx :
        min_value = min(min_value, result)
        max_value = max(max_value, result)
        return

    if arr[0]!= 0 :
        arr[0] -= 1
        dfs(arr, result + nums[idx], idx+1)
        arr[0] +=1

    if arr[1] != 0 :
        arr[1] -= 1
        dfs(arr, result - nums[idx], idx+1)
        arr[1] += 1

    if arr[2] != 0 :
        arr[2] -= 1
        dfs(arr, result * nums[idx], idx+1)
        arr[2] += 1

    if arr[3] != 0 :
        arr[3] -= 1
        if result < 0 :
            dfs(arr, -(-result // nums[idx]), idx+1)
        else :
            dfs(arr, result // nums[idx], idx+1)
        arr[3] += 1

dfs(arr, nums[0], 1)
print(max_value)
print(min_value)