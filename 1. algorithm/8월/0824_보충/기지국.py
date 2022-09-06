import sys; sys.stdin = open('123.txt', 'r')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def check(x, y):
    for i in range(4):
        for j in range(1, ord(arr[x][y]) - ord('A') + 2):
            nx = x + dx[i] * j
            ny = y + dy[i] * j
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] == 'H':
                    arr[nx][ny] = 'X'

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'A' or arr[i][j] == 'B' or arr[i][j] == 'C':
                x, y = i, j
                check(x, y)

    Hcnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':
                Hcnt += 1

    print(f'#{tc} {Hcnt}')
