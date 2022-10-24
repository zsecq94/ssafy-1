# import sys; sys.stdin = open('123.txt', 'r')
from collections import deque

def find_road(x, y):
    q = deque()
    q.append((x, y))
    visited = [[False] * M for _ in range(N)]
    visited[x][y] = True
    ans = [[0] * M for _ in range(N)]
    while q:
        xx, yy = q.popleft()
        for xxx, yyy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx = xx + xxx
            ny = yy + yyy
            if 0<=nx<N and 0<=ny<M and arr[nx][ny] != 0 and visited[nx][ny] == False:
                ans[nx][ny] = ans[xx][yy] + 1
                visited[nx][ny] = True
                q.append((nx, ny))
    maxVV = 0
    for w in range(N):
        for e in range(M):
            if maxVV < ans[w][e]:
                maxVV = ans[w][e]
    return maxVV

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            arr[i][j] = 1
        else:
            arr[i][j] = 0

maxV = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] != 0:
            a = find_road(i, j)
            if maxV < a:
                maxV = a
print(maxV)