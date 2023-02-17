# import sys; sys.stdin = open('123.txt', 'r')
from collections import deque

def go(i, j):
    cnt = 1
    q = deque()
    q.append((i, j))
    while q:
        x, y = q.popleft()
        for xx, yy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx = x + xx
            ny = y + yy
            if 0<=nx<M and 0<=ny<N and arr[nx][ny] == 0:
                q.append((nx, ny))
                arr[nx][ny] = 99
                cnt += 1
    if cnt > 1:
        cnt -= 1
    return cnt


M, N, K = map(int, input().split())
arr = [[0] * N for _ in range(M)]
for k in range(K):
    a, b, c, d = map(int, input().split())
    for i in range(b, d):
        for j in range(a, c):
            arr[i][j] = 1
result = []
for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            result.append(go(i, j))

result = sorted(result)
print(len(result))
for i in result:
    print(i, end=' ')
print()