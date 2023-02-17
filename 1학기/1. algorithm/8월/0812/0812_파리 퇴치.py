import sys
sys.stdin = open('123.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    maxV = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            sumV = 0
            for a in range(M):
                for b in range(M):
                    sumV += arr[i+a][j+b]
            if maxV < sumV:
                maxV = sumV

    print(f'#{tc} {maxV}')


