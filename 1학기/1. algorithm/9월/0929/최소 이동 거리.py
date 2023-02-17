# import sys; sys.stdin = open('123.txt', 'r')

def dijk():
    U = []
    D = [10000] * (N+1)
    D[0] = 0
    while len(U) < (N+1):
        minV = 10000
        for i in range(N+1):
            if i in U: continue
            if minV > D[i]:
                minV = D[i]
                curV = i

        U.append(curV)

        for i in range(N+1):
            if i in U: continue
            if G[curV][i]:
                D[i] = min(D[i], D[curV] + G[curV][i])
    print(f'#{tc} {D[-1]}')

for tc in range(1, int(input())+1):
    N, E = map(int, input().split())
    G = [[0] * (N+1) for _ in range(N+1)]

    for i in range(E):
        s, e, w = map(int, input().split())
        G[s][e] = w
    dijk()