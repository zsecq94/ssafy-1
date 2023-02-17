import sys
sys.stdin = open('123.txt', 'r')

def pos(root):
    if root <= N+1:
        pos(tree[root][2])
        pos(tree[root][3])
        if tree[root][1] == '-':
            tree[root][1] = tree[root][2] - tree[root][3]
        # elif tree[root][1] == '+':
        #     tree[root] = tree[root][0] + tree[root][1]
        # elif tree[root][1] == '*':
        #     tree[root] = tree[root][0] * tree[root][1]
        # elif tree[root][1] == '/':
        #     tree[root] = tree[root][0] // tree[root][1]

T = 5
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
    print(tree)
    # pos(1)



    # print(tree)

    # pos(1)
    # print(tree)
