import sys; sys.stdin = open('123.txt', 'r')

di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]

def miro(x, y):
    q = []
    q.append((x, y))
    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx = x + di[i]
            ny = y + dj[i]
            if arr[nx][ny] == 3:
                return 1
            else:
                if arr[nx][ny] == 0:
                    q.append((nx, ny))
                    arr[nx][ny] = 1
    return 0

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(16)]

    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                x, y = i, j

    print(f'#{tc} {miro(x, y)}')