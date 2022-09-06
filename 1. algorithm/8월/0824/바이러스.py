import sys; sys.stdin = open('123.txt', 'r')

def bfs(N):
    visited = [[0]*N for _ in range(N)]
    q = []
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                q.append((i,j))
                visited[i][j] = 1
    while q:
        i, j = q.pop(0)

        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, i+dj
            if maze[ni][nj] != 1 and visited[ni][nj] == 0:  # 벽으로 둘러쌓인 미로기때문에 벽 검사 ㄴ
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    print(f'#{tc} {bfs(N)}')