import sys; sys.stdin = open('123.txt', 'r')

def melt(x, y):
    zero_cnt = 0
    for xx, yy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx = x + xx
        ny = y + yy
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
            zero_cnt += 1
    return zero_cnt

def asd():
    cnt = 0
    while True:
        lst = []
        for i in range(n):
            for j in range(m):
                if arr[i][j] != 0:
                    if melt(i, j) == 4:
                        return cnt
                    else:
                        lst.append(melt(i, j))

        a = 0
        for q in range(n):
            for w in range(m):
                if arr[q][w] != 0:
                    if arr[q][w] - lst[a] < 0:
                        arr[q][w] = 0
                    else:
                        arr[q][w] -= lst[a]
                    a += 1
        cnt += 1

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

result = asd()
print(result)