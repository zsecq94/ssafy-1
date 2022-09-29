import sys; sys.stdin = open('123.txt', 'r')

def dijk(gr):
    U = [False] * (N+1)
    D = [100000] * (N+1)
    D[X] = 0

    while U.count(True) < N:
        minV = 100000

        for i in range(N+1):
            if U[i]: continue
            if minV > D[i]:
                minV = D[i]
                curV = i

        U[curV] = True

        for i in range(N+1):
            if U[i]: continue
            D[i] = min(D[i], D[curV]+gr[curV][i])

    return D


for tc in range(1, int(input())+1):
    N, M, X = map(int, input().split())
    G1 = [[100000]*(N+1) for _ in range(N+1)]
    G2 = [[100000]*(N+1) for _ in range(N+1)]

    for i in range(M):
        x, y, c = map(int, input().split())
        G1[x][y] = c
        G1[y][x] = c

    a = dijk(G1)
    b = dijk(G2)

    print(a)
    print(b)