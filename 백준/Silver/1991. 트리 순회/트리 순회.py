import sys
input = sys.stdin.readline

n = int(input())

def preorder(x):
    print(x, end='')
    if tree[x][0] != '.':
        preorder(tree[x][0])
    if tree[x][1] != '.':
        preorder(tree[x][1])

def inorder(x):
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

tree = {}

for _ in range(n):
    a, b, c = input().split()

    tree[a] = (b, c)

preorder('A')
print()
inorder('A')
print()
postorder('A')