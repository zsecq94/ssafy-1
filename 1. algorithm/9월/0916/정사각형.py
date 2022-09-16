import copy
import sys; sys.stdin = open('123.txt', 'r')

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

def asd(x, y):
    global test
    cnt = 1
    st = []
    st.append((x, y))
    while st:
        ii, jj = st.pop(0)
        for i in range(4):
            ni = ii + dx[i]
            nj = jj + dy[i]
            if 0<=ni<N and 0<=nj<N:
                if arr[x][y]+1 == arr[ni][nj]:
                    st.append((ni, nj))
                    # arr[x][y] = -1
                    x, y = ni, nj
                    cnt += 1
                    break
    return cnt

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    test = copy.deepcopy(arr)

    num = 999999
    result = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0:
                x, y = i, j
                cntV = asd(x, y)
                if result < cntV:
                    result = cntV
                    num = test[i][j]
                if result == cntV and num > test[i][j]:
                    num = test[i][j]

    print(f'#{tc} {num} {result}')