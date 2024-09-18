import sys
input = sys.stdin.readline

def preorder(x):
    print(x, end='')
    if tree[x][0] != '.' :
        preorder(tree[x][0])
    if tree[x][1] != '.' :
        preorder(tree[x][1])

def inorder(x) :
    if tree[x][0] != '.':
        inorder(tree[x][0])
    print(x, end='')
    if tree[x][1] != '.':
        inorder(tree[x][1])

def postorder(x):
    if tree[x][0] != '.':
        postorder(tree[x][0])
    if tree[x][1] != '.':
        postorder(tree[x][1])
    print(x, end='')

n = int(input())

tree = {}

for _ in range(n):
    root, left, right = input().split()
    tree[root] = [left, right]


preorder('A')
print()
inorder('A')
print()
postorder('A')