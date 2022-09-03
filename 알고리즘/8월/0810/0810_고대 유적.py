T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    maxV = 0
    for i in range(N):
        for j in range(len(arr)):
            if 