import sys
sys.stdin = open('123.txt', 'r')


def cal(lv, rv, ca):
    if ca == '-':
        return lv - rv
    elif ca == '+':
        return lv + rv
    elif ca == '*':
        return lv * rv
    else:
        return lv // rv

def pos(root):
    if root <= N:
        if type(tree[root][1]) == int:
            return tree[root][1]
        else:
            ca = tree[root][1]
            lv = pos(tree[root][2])
            rv = pos(tree[root][3])
            return cal(lv, rv, ca)

T = 10
for tc in range(1, T+1):
    N = int(input())
    tree = [[] for _ in range(N+1)]

    for i in range(N):
        arr = input().split()
        v = int(arr[0])

        for j in arr:
            if j.isdigit():
                tree[v].append(int(j))
            else:
                tree[v].append(j)

    print(f'#{tc} {pos(1)}')