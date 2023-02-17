import sys; sys.stdin = open('123.txt', 'r')

def ino(root):
    if root:
        ino(tree[root][1])
        print(tree[root][0], end='')
        ino(tree[root][2])

T = 10
for tc in range(1, T+1):
    N = int(input())
    tree = [[0, 0, 0] for _ in range(N+1)]
    arr = [list(input().split()) for _ in range(N)]
    print(f'#{tc}', end=' ')
    for i in range(len(arr)):
        if len(arr[i]) == 4:
            tree[i+1][0] = arr[i][1]
            tree[i+1][1] = int(arr[i][2])
            tree[i+1][2] = int(arr[i][3])
        if len(arr[i]) == 3:
            tree[i+1][0] = arr[i][1]
            tree[i+1][1] = int(arr[i][2])
        else:
            tree[i+1][0] = arr[i][1]
    ino(1)
    print()