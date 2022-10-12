import sys; sys.stdin = open('123.txt', 'r')

def melt(x, y):
    a = 1
    for xx, yy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx = x + xx
        ny = y + yy
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == a-1:
            arr[x][y] = a-1
            a += 1
            return

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            melt(i, j)