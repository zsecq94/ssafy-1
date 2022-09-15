import sys; sys.stdin = open('123.txt', 'r')

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def asd(x, y):
    global cnt
    test[x][y] = 0
    st = []
    st.append((x, y))
    while st:
        ii, jj = st.pop(0)
        for i in range(4):
            ni = ii + dx[i]
            nj = jj + dy[i]
            if 0 <= ni < N and 0 <= nj < N:
                if test[ni][nj] != 0:
                    st.append((ni, nj))
                    test[ni][nj] = 0
    cnt += 1
    return

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
test = [[0] * N for _ in range(N)]
cntV = 0

maxV = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] > maxV:
            maxV = arr[i][j]

rangE = 0
for k in range(1, maxV+1):
    for i in range(N):
        for j in range(N):
            test[i][j] = arr[i][j]
            if test[i][j] <= k:
                test[i][j] = 0

    cnt = 0
    for q in range(N):
        for w in range(N):
            if test[q][w] != 0:
                x, y = q, w
                asd(x, y)

    if cntV < cnt:
        cntV = cnt

if cntV == 0:
    print(1)
else:
    print(cntV)