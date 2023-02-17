import sys; sys.stdin = open('123.txt', 'r')

def pre(root):
    global cnt
    if root:
        cnt += 1
        pre(tree[root][0])
        pre(tree[root][1])

for tc in range(1, int(input())+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))

    V = E+1
    tree = [[0, 0] for _ in range(V+1)]

    for i in range(0, len(arr), 2):
        a, b = arr[i], arr[i+1]
        if tree[a][0] == 0:
            tree[a][0] = b
        else:
            tree[a][1] = b

    cnt = 0
    pre(N)
    print(f'#{tc} {cnt}')