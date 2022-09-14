import sys; sys.stdin = open('123.txt', 'r')

# 노드의 개수 N과 리프 노드의 개수 M, 값을 출력할 노드 번호 L
def ino(root):
    if root <= a:
        if not tree[root]:
            ino(root*2)
            ino(root*2+1)
            tree[root] = tree[root*2] + tree[root*2+1]

T = int(input())
for tc in range(1, T+1):
    n, m, l = map(int, input().split())
    tree = [0] * 1001
    for i in range(m):
        arr = list(map(int, input().split()))
        tree[arr[0]] = arr[1]

    a = 0
    for i in range(len(tree)):
        if tree[i] != 0:
            a = tree.index(tree[i])

    ino(1)
    print(f'#{tc} {tree[l]}')
