import sys; sys.stdin = open('123.txt', 'r')

dx = [0, 1, 1]
dy = [1, 1, 0]
def bfs(x, y):
    st = [(x, y)]
    visit = [[0] * N for _ in range(N)]
    visit[0][0] = 2
    visit[0][1] = 2
    cnt = 0
    while st:
        ii, jj = st.pop(0)
        if arr[ii][jj] == 2 and arr[ii][jj-1] == 2:
            for i in range(2):
                nx = ii+dx[i]
                ny = jj+dy[i]
                if nx < N and ny < N:
                    if arr[nx][ny] == 1:
                        return cnt
                    else:
                        visit[nx][ny] = 2
                        st.append((nx, ny))
        elif arr[ii][jj] == 2 and arr[ii+1][jj+1] == 2:
            for i in range(3):
                nx = ii + dx[i]
                ny = jj + dy[i]
                if nx < N and ny < N:
                    if arr[nx][ny] == 0:
                        visit[nx][ny] = 2
                        st.append((nx, ny))

    return cnt
for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]


    print(bfs(0, 1))