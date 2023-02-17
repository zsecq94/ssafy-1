import sys; sys.stdin = open('123.txt', 'r')

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

def asd(x, y, doll, doll1):
    arr[x][y] = doll

    for i in range(8):
        st = []
        ni = x + dx[i]
        nj = y + dy[i]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == doll1:
            while 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == doll1:
                st.append((ni, nj))
                ni += dx[i]
                nj += dy[i]
                if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == doll:
                    while st:
                        xx, yy = st.pop(0)
                        arr[xx][yy] = doll


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]
    for i in range(N//2-1, N//2+1):
        for j in range(N//2-1, N//2+1):
            if i == j:
                arr[i][j] = 2
            else:
                arr[i][j] = 1
    doll1 = 0
    for i in range(M):
        x, y, doll = map(int, input().split())
        if doll == 1:
            doll1 = 2
        elif doll == 2:
            doll1 = 1
        asd(x-1, y-1, doll, doll1)

    cntB = 0
    cntW = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                cntB += 1
            elif arr[i][j] == 2:
                cntW += 1

    print(f'#{tc} {cntB} {cntW}')
