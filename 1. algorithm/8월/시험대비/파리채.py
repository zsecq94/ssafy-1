import sys
sys.stdin = open('123.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    maxV = 0
    for i in range(0, N-M+1):
        for j in range(0, N-M+1):
            sumV = 0
            for ii in range(i, i+M):
                for jj in range(j, j+M):
                    sumV += arr[ii][jj]
            if maxV < sumV:
                maxV = sumV
    print(f'#{tc} {maxV}')