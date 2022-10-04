import sys; sys.stdin = open('123.txt', 'r')

def prim():
    U = []
    D = [10000] * (N+1)
    D[0] = 0
    while len(U) < (N+1):
        # curV = U에 D중 가장 작은 값을 가진 정점을 선택
        minV = 10000
        for i in range(N+1):
            if i in U: continue
            if minV > D[i]:
                minV = D[i]
                curV = i

        U.append(curV)
        # curV하고 연결된 정점들의 D갑을 최선으로 변경
        for i in range(N+1):
            if i in U: continue
            if G[curV][i] and D[i] > G[curV][i]:
                D[i] = G[curV][i]
    print(U, D)



N, E = map(int, input().split())
G = [[0] * (N+1) for _ in range(N+1)]

for i in range(E):
    n1, n2, w = map(int, input().split())
    G[n1][n2] = w

prim()