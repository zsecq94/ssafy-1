
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def atk(x, y):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        while True:
            if 0 <= nx < N and 0 <= ny < N and (arr[nx][ny] == 0 or arr[nx][ny] == 3):
                arr[nx][ny] = 3
                nx = nx + dx[i]
                ny = ny + dy[i]
            else:
                break


for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                atk(i, j)

    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                cnt += 1

    print(f'#{tc} {cnt}')