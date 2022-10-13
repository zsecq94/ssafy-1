import sys; sys.stdin = open('123.txt', 'r')
from collections import deque
def melt(i, j):
    visited = [[False] * m for _ in range(n)]
    visited[i][j] = True
    q = deque()
    q.append((i, j))
    while q:
        x, y = q.popleft()
        for xx, yy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx = x + xx
            ny = y + yy
            if 0<=nx<n and 0<=ny<m and visited[nx][ny] == False:
                if arr[nx][ny] == 1:
                    arr[nx][ny] = 0
                    visited[nx][ny] = True
                else:
                    q.append((nx,ny))
                    visited[nx][ny] = True

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cheeze_lst = [0]
while True:
    cheeze_cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                cheeze_cnt += 1
    if cheeze_cnt == 0:
        break
    cheeze_lst.append(cheeze_cnt)
    melt(0, 0)

print(len(cheeze_lst)-1)
print(cheeze_lst[-1])