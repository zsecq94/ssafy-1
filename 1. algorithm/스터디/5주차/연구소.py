import sys; sys.stdin = open('123.txt', 'r')
from collections import deque

def bfs():
    q = deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                q.append((i, j))
    while q:
        x, y = q.popleft()
        for xx, yy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx = x + xx
            ny = y + yy
            if 0<=nx<N and 0<=ny<M and arr[nx][ny] == 0:
                arr[nx][ny] = 2
                q.append((nx, ny))


def wall(count):
    global maxV
    cnt = 0
    if count == 3:
        bfs()
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 0:
                    cnt += 1
        if maxV < cnt:
            maxV = cnt
        return
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                wall(count+1)
                arr[i][j] = 0

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
maxV = 0
wall(cnt)

print(maxV)