import sys; sys.stdin = open('123.txt', 'r')

def turn_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret

def turn_180(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[N-1-r][N-1-c] = m[r][c]
    return ret

def turn_270(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[N-1-c][r] = m[r][c]
    return ret

dx = [0]
dy = [1]
def go(i, j):
    newArr[i].append(0)
    st = [(i, j)]
    while st:
        ii, jj = st.pop(0)
        for i in range(1):
            nx = ii + dx[i]
            ny = jj + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if newArr[ii][jj] == newArr[nx][ny]:
                    newArr[ii][jj] = newArr[ii][jj]*2
                    newArr[nx].pop(ny)
                    newArr[ii].append(0)
                    st.append((nx, ny))
                elif newArr[ii][jj] == 0:
                    newArr[ii].pop(jj)
                    newArr[ii].append(0)
                    st.append((ii, jj))
                elif newArr[nx][ny] == 0:
                    if newArr[nx][ny+1] != 0:
                        newArr[nx].pop(ny)
                        newArr[nx].append(0)
                        st.append((ii, jj))
                    else:
                        newArr[nx].pop(ny)
                        newArr[nx].append(0)
                        st.append((nx, ny))
                else:
                    st.append((nx, ny))

for tc in range(1, int(input())+1):
    N, S = input().split()
    N = int(N)
    arr = [list(map(int, input().split())) for _ in range(N)]

    if S == 'up':
        newArr = turn_270(arr)
        for i in range(N):
            for j in range(1):
                go(i, j)
        ARR = turn_90(newArr)
        print(f'#{tc}')
        for i in range(N):
            for j in range(N):
                print(ARR[i][j], end= ' ')
            print()

    elif S == 'down':
        newArr = turn_90(arr)
        for i in range(N):
            for j in range(1):
                go(i, j)
        ARR1 = turn_270(newArr)
        print(f'#{tc}')
        for i in range(N):
            for j in range(N):
                print(ARR1[i][j], end=' ')
            print()

    elif S == 'right':
        newArr = turn_180(arr)
        for i in range(N):
            for j in range(1):
                go(i, j)
        ARR1 = turn_180(newArr)
        print(f'#{tc}')
        for i in range(N):
            for j in range(N):
                print(ARR1[i][j], end=' ')
            print()

    else:
        newArr = arr
        for i in range(N):
            for j in range(1):
                go(i, j)
        ARR1 = newArr
        print(f'#{tc}')
        for i in range(N):
            for j in range(N):
                print(ARR1[i][j], end=' ')
            print()
