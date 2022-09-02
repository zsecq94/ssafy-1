import sys; sys.stdin = open('123.txt', 'r')

di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]

def tel(x, y):
    for i in range(4):
        for j in range(1, ord(arr[x][y]) - 63):
            ni = x + di[i] * j
            nj = y + dj[i] * j
            if 0 <= ni < 10 and 0 <= nj < 9:
                if arr[ni][nj] == 'H':
                    arr[ni][nj] = 'X'

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N+1)]

    for i in range(N+1):
        for j in range(N):
            if arr[i][j] == 'A' or arr[i][j] == 'B' or arr[i][j] == 'C':
                x, y = i, j
                tel(x, y)

    Hcnt = 0
    for i in range(N+1):
        for j in range(N):
            if arr[i][j] == 'H':
                Hcnt += 1

    print(f'#{tc} {Hcnt}')