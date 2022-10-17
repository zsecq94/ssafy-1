import copy
# import sys; sys.stdin = open('123.txt', 'r')
from collections import deque

def find_zero(arr1):
    global result
    zero_cnt = 0
    for i in range(n):
        for j in range(m):
            if arr1[i][j] == 0:
                zero_cnt += 1
    if result < zero_cnt:
        result = zero_cnt

def bfs(i, j, arr1):
    q = deque()
    q.append((i, j))
    while q:
        xx, yy = q.popleft()
        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx = x + xx
            ny = y + yy
            if 0<=nx<n and 0<=ny<m and arr1[nx][ny] == 0:
                arr1[nx][ny] = 3
                q.append((nx, ny))
    return arr1

def wall(V):
    a = []
    if V == 3:
        arr1 = copy.deepcopy(arr)
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 2:
                    a = bfs(i, j, arr1)
        find_zero(a)
        return
    else:
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 0:
                    arr[i][j] = 1
                    wall(V+1)
                    arr[i][j] = 0

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
result = 0
wall(cnt)

print(result)