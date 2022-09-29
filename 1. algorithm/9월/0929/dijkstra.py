import sys; sys.stdin = open('123.txt', 'r')

def dijk():
    U = []
    D = [10000] * (N+1)
    D[0] = 0
    while len(U) < (N+1):
        # D최소값을 구한다.
        minV = 10000
        for i in range(N+1):
            if i in U: continue
            if minV > D[i]:
                minV = D[i]
                curV = i

        U.append(curV)

        # D를 수정
        for i in range(N+1):
            if i in U: continue
            # if G[curV][i] and D[i] > D[curV] + G[curV][i]:
            #     D[i] = D[curV] + G[curV][i]
            if G[curV][i]:
                D[i] = min(D[i], D[curV] + G[curV][i])

    print(U, D)


N, E = map(int, input().split())
G = [[0] * (N+1) for _ in range(N+1)]

for i in range(E):
    n1, n2, w = map(int, input().split())
    G[n1][n2] = w
    # G[n2][n1] = w : 방향성이 있기 때문에 불필요

print(G)
dijk()