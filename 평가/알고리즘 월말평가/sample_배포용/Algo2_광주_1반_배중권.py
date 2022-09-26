import sys; sys.stdin = open('algo2_sample_in.txt', 'r')

def pre(root):
    cntA.append(root)
    if tree[root]:
        pre(tree[root][0])
        pre(tree[root][1])


for tc in range(1, int(input())+1):
    N = int(input())
    tree = [[] for _ in range(N+1)]

    a = 1
    for i in range(2, N+1):
        if len(tree[a]) >= 2:
            a += 1
        tree[a].append(i)

    cntA = []
    cntB = []
    cntC = []
    pre(1)
    print(cntA)