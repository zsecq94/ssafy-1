import sys; sys.stdin = open('123.txt', 'r')
from collections import deque
import copy

def find_result(arr):
    global cnt
    zero_cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                zero_cnt += 1
    if cnt > zero_cnt:
        cnt = zero_cnt



def go(lst):
    if not lst:
        return
    q = deque(lst)
    x, y = q.popleft()
    arr = copy.deepcopy(arr)
    if arr[x][y] == 1:
        for xx, yy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx = x + xx
            ny = y + yy
            if 0<=nx<N and 0<=ny<M and arr[nx][ny] == 0:
                arr[nx][ny] = 'C'
                qq = deque()
                qq.append((nx, ny))
                while qq:
                    xx, yy = qq.popleft()
                    ni = nx + xx
                    nj = ny + yy
                    if 0<=ni<N and 0<=nj<M and arr[nx][ny] == 0:
                        arr[ni][nj] = 'C'
                        qq.append((ni, nj))
                go(q)
                find_result(arr)



N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
lst = []
cnt = N * M
for i in range(N):
    for j in range(M):
        if arr[i][j] != 0 and arr[i][j] != 6:
            lst.append((i, j))

go(lst)