import sys; sys.stdin = open('123.txt', 'r')
from collections import deque

def asd(x, y):
    q = deque()
    q.append((x, y))
    dis[0][0] = 0
    while q:
        xx, yy = q.popleft()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx = xx+dx
            ny = yy+dy
            if 0 <= nx < N and 0 <= ny < N:
                gap = max(arr[nx][ny] - arr[xx][yy], 0) + 1
                if dis[nx][ny] > dis[xx][yy] + gap:
                    dis[nx][ny] = dis[xx][yy] + gap
                    q.append((nx, ny))
    return dis[-1][-1]

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dis = [[99999] * N for _ in range(N)]
    a = asd(0, 0)
    print(f'#{tc} {a}')


