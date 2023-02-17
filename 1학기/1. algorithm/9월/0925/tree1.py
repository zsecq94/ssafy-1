import sys; sys.stdin = open('123.txt', 'r')

def pre(root):
    if root:
        print(root, end=' ')
        pre(tree[root][0])
        pre(tree[root][1])


for tc in range(1, 3):
    V, E = map(int, input().split())
    tree = [[0, 0] for _ in range(V+1)]
    arr = list(map(int, input().split()))

    for i in range(0, len(arr), 2):
        a, b = arr[i], arr[i+1]
        if tree[a][0] == 0:
            tree[a][0] = b
        else:
            tree[a][1] = b
    print(f'#{tc}', end=' ')
    print(tree)
    pre(1)
    print()