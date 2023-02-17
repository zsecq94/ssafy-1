import sys
sys.stdin = open('123.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))

    maxV = 0
    minV = 0

    # 초기값
    for j in range(M):
        maxV += Ai[j]
        minV += Ai[j]

    # 2번째 경우의수부터
    for i in range(1, N-M+1):
        sumV = 0
        # M개의 구간합을 구함
        for j in range(i, i+M):
            sumV += Ai[j]
        # maxV 값을 최신화
        if maxV < sumV:
            maxV = sumV
        # minV 값을 최신화
        if minV > sumV:
            minV = sumV

    print(f'#{tc} {maxV - minV}')