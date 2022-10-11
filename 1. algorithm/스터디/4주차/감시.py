import sys; sys.stdin = open('123.txt', 'r')

def go(x, y):
    five_cnt = 0
    if arr[x][y] == 5:
        for xx, yy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx = x + xx
            ny = y + yy
            while 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != 6:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = 5
                    five_cnt += 1
                nx += xx
                ny += yy

    four_cnt = 0
    if arr[x][y] == 4:
        cnt = 0
        for xx, yy in [(0, -1), (-1, 0), (0, 1)]:
            nx = x + xx
            ny = y + yy
            while 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != 6:
                if arr[nx][ny] == 0:
                    cnt += 1
                nx += xx
                ny += yy





n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

zero_cnt = 0
v = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            zero_cnt += 1
        elif arr[i][j] == 5:
            v += go(i, j)

for i in range(n):
    for j in range(m):
        if arr[i][j] == 4:
            v += go(i, j)


print(zero_cnt - v)