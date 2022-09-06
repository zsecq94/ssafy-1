import sys; sys.stdin = open('123.txt', 'r')

dx1 = [0, 0, 1, -1]
dy1 = [-1, 1, 0, 0]
dx2 = [1, 1, -1, -1]
dy2 = [1, -1, -1, 1]

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    maxV = 0
    for i in range(n):
        for j in range(n):
            cnt1 = arr[i][j]
            for k in range(4):
                for z in range(1, m):
                    nx, ny = i+dx1[k]*z, j+dy1[k]*z
                    if 0 <= nx < n and 0 <= ny < n:
                        cnt1 += arr[nx][ny]
            if maxV < cnt1:
                maxV = cnt1
            cnt2 = arr[i][j]
            for k in range(4):
                for z in range(1, m):
                    nx, ny = i+dx2[k]*z, j+dy2[k]*z
                    if 0 <= nx < n and 0 <= ny < n:
                        cnt2 += arr[nx][ny]
            if maxV < cnt2:
                maxV = cnt2

    print(f'#{tc} {maxV}')