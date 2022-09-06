import sys; sys.stdin = open('123.txt', 'r')

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def find(x, y):
    for i in range(4):
        for j in range(1, k+1):
            nx = x + dx[i] * j
            ny = y + dy[i] * j
            if nx >= 0 and ny >= 0 and nx < n and ny < n:
                if arr[nx][ny] == 'H':
                    arr[nx][ny] = 'X'

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'A':
                x, y = i, j
                k = 1
                find(x, y)

            elif arr[i][j] == 'B':
                x, y = i, j
                k = 2
                find(x, y)

            elif arr[i][j] == 'C':
                x, y = i, j
                k = 3
                find(x, y)

    cnt = 0
    for ii in range(n):
        for jj in range(n):
            if arr[ii][jj] == 'H':
                cnt += 1

    print(f'#{tc} {cnt}')