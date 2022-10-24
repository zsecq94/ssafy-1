import sys; sys.stdin = open('123.txt', 'r')
from collections import deque
import copy

def check(arr1):
    global cnt
    zero_cnt = 0
    for i in range(N):
        for j in range(M):
            if arr1[i][j] == 0:
                zero_cnt += 1
    if cnt > zero_cnt:
        cnt = zero_cnt

def bfs():
    global q
    while q:
        i, j = q.pop()
        if arr[i][j] == 1:
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx = i + x
                ny = j + y
                while 0<=nx<N and 0<=ny<M and arr[nx][ny] == 0:
                    arr[nx][ny] = 1
                    nx += x
                    ny += y
                bfs()
                check(arr)
                nx -= x
                ny -= y
                while 0<=nx<N and 0<=ny<M and arr[nx][ny] == 1:
                    arr[nx][ny] = 0
                    nx -= x
                    ny -= y
                arr[i][j] = 1



N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

q = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] != 0 and arr[i][j] != 6:
            q.append((i, j))
cnt = N * M
bfs()
print(cnt)