import sys; sys.stdin = open('123.txt', 'r')

# def find(kV):




T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    CITY = [list(map(int, input().split())) for _ in range(N)]
    HOMES = []
    for r in range(N):
        for c in range(N):
            if CITY[r][c] == 1:
                HOMES.append((r, c))

    for row in range(N):
        for col in range(N):
            result = find(row, col)