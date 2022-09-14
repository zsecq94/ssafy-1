import sys; sys.stdin = open('123.txt', 'r')

def ino(root):
    if root <= N:
        ino(root*2)
        ino(root*2+1)
        if tree[root] == '-':
            tree[root] = tree[root*2] - tree[root*2+1]
        elif tree[root] == '+':
            tree[root] = tree[root*2] + tree[root*2+1]
        elif tree[root] == '*':
            tree[root] = tree[root*2] * tree[root*2+1]
        elif tree[root] == '/':
            tree[root] = tree[root*2] // tree[root*2+1]

T = 10
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)

    for i in range(1, N+1):
        arr = input().split()
        if arr[1].isdigit():
            tree[i] = int(arr[1])
        else:
            tree[i] = arr[1]

    ino(1)
    print(tree[1])