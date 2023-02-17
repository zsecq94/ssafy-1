import sys; sys.stdin = open('123.txt', 'r')
from collections import deque

def solve():
    Q = deque()
    Q.append((N, 0))
    while Q:
        v, cnt = Q.popleft()
        for newV in [v*2, v-10, v+1, v-1]:
            if newV == M:
                return cnt+1
            if 0 < newV <= 1000000 and visited[newV] == 0:
                Q.append((newV, cnt+1))
                visited[newV] = 1
    return -1


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    visited = [0] * 1000001
    print(f'#{tc} {solve()}')