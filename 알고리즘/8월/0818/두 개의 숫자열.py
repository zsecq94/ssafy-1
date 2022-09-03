import sys
sys.stdin = open('123.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))

    Z = 0
    X = 0
    if len(Ai) > len(Bj):
        Z = Ai
        X = Bj
    else:
        Z = Bj
        X = Ai

    maxV = 0
    for i in range(len(Z)-len(X)+1):
        sumV = 0
        for j in range(len(X)):
            sumV += X[j] * Z[j+i]
        if maxV < sumV:
            maxV = sumV
    print(f'#{tc} {maxV}')