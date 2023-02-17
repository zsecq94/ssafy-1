# import sys; sys.stdin = open('123.txt', 'r')
from collections import deque

def miro(i, j):
    q = deque()
    q.append((i, j))
    while q:
        xx, yy = q.popleft()
        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx = xx + x
            ny = yy + y
            if 0<=nx<100 and 0<=ny<100:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = 99
                    q.append((nx, ny))
                if arr[nx][ny] == 3:
                    return 1
    return 0



for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(100)]


    for i in range(100):
        for j in range(100):
            if arr[i][j] == 2:
                print(f' #{tc} {miro(i, j)}')