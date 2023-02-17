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
            if arr[nx][ny] == -1:
                arr[nx][ny] = arr[x][y] + 1
                return arr[nx][ny] - 3
            else:
                if arr[nx][ny] == 0:
                    q.append((nx, ny))
                    arr[nx][ny] = arr[x][y] + 1
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[1] * (N+2)] + [[1] + list(map(int, input())) + [1] for _ in range(N)] + [[1] * (N+2)]

    x = 0
    y = 0
    for i in range(N+2):
        for j in range(N+2):
            if arr[i][j] == 2:
                x, y = i, j
            if arr[i][j] == 3:
                arr[i][j] = -1

    print(f'#{tc} {miro(x, y)}')
