import sys
sys.stdin = open('123.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    maxC = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
                if maxC < cnt:
                    maxC = cnt
            else:
                cnt = 0

    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[j][i] == 1:
                cnt += 1
                if maxC < cnt:
                    maxC = cnt
            else:
                cnt = 0

    print(f'#{tc} {maxC}')