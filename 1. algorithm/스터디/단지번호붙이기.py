import sys; sys.stdin = open('123.txt', 'r')

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def asd(x, y):
    global cntV
    cnt = 1
    arr[x][y] = 0
    st = []
    st.append((x, y))
    while st:
        ii, jj = st.pop(0)
        for i in range(4):
            ni = ii + dx[i]
            nj = jj + dy[i]
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] == 1:
                    st.append((ni, nj))
                    arr[ni][nj] = 0
                    cnt += 1
    cntV += 1
    return cnt

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
result = []
cntV = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            x, y = i, j
            result.append(asd(x, y))
result = sorted(result)
print(cntV)
for i in result:
    print(i)