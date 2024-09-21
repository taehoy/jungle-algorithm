import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
from collections import deque

n = int(input())

s = input().rstrip()
inout = [-1]
for i in range(len(s)):
    inout.append(int(s[i]))

graph = [[] for _ in range(n+1)]

while True :
    try :
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    except :
        break

count = 0

def dfs(first):
    global count 

   
    
    stack = [first]
    visited[first] = True

    while stack :
        now = stack.pop()

        for next in graph[now]:
            if not visited[next]:
                # 실내 -> 실내 : 종료
                if inout[now] == 1 and inout[next] == 1 :
                    count +=1
                    continue
                # 실내 -> 실외
                elif inout[now] == 1 and inout[next] == 0 :
                    stack.append(next)
                    visited[next] = True
                # 실외 -> 실내 : 다음 장소가 끝장소
                elif inout[now] == 0 and inout[next] == 1:
                    count +=1
                    continue
                # 실외 -> 실외
                elif inout[now] == 0 and inout[next] == 0 :
                    stack.append(next)
                    visited[next] = True

for i in range(1, n+1):
    # 처음이 실외면 패스
    if inout[i] == 0 :
        continue
    visited = [False] * (n+1)
    if not visited[i] :
        dfs(i)

print(count)