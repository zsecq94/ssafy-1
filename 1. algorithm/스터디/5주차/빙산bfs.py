import sys; sys.stdin = open('123.txt', 'r')
import copy

def bfs(x, y):
    q = [(x, y)]
    while q:
        zero_cnt = 0
        xx, yy = q.pop(0)
        for ii, jj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx = xx + ii
            ny = yy + jj
            if 0<=nx<n and 0<=ny<m and arr[nx][ny] == 0:
                zero_cnt += 1
                q.append((nx, ny))
        arr1[xx][yy] -= zero_cnt





n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
arr1 = copy.deepcopy(arr)

while True:
    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0:
                bfs(i, j)