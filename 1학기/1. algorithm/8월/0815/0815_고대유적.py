import sys
sys.stdin = open("123.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    maxV = 0
    for i in range(N):
        cnt = 0
        cnt1 = 0
        for j in range(M):
            if arr[i][j] == 1:
                cnt += 1
                if maxV < cnt:
                    maxV = cnt
            if arr[j][i] == 1:
                cnt1 += 1
                if maxV < cnt1:
                    maxV = cnt1
            else:
                cnt = 0
                cnt1 = 0

    print(f'#{tc} {maxV}')