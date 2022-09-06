import sys; sys.stdin = open('123.txt', 'r')

def bfs(i, j, N):


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input().split())) for _ in range(N)]

    sti = -1
    stj = -1
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sti, stj = i, j
                break
        if sti != -1:
            break
    print(sti, stj)

    # print(f'#{tc} {bfs(sti, stj, N)}')