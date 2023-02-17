import sys; sys.stdin = open('123.txt', 'r')
    # 우 하 좌 상
dr = [0, +1, 0, -1]
dc = [+1, 0, -1, 0]
# 2에서 3까지 갈 수 있으면 1 아니면 0을 리턴
def dfs(curR, curC):
    visited = [[False] * N for _ in range(N)]
    st = []

    # 1. 스택에 시작점을 push, 시작점 방문표시
    st.append((curR, curC))
    visited[curR][curC] = True

    # 2. 스택에 데이터가 있는 동안
    while st:
        curR, curC = st.pop()

        # cur와 연결된 모든 포인트에 대하여
        for d in range(4):
            newR = curR + dr[d]
            newC = curC + dc[d]

            # new 가 이동이 가능하면(선이 연결되어 있으면)
            if 0 <= newR < N and 0 <= newC < N and arr[newR][newC] != 1 and not visited[newR][newC]:
                if arr[newR][newC] == 3:
                    return 1
                st.append((newR, newC))
                visited[newR][newC] = True
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                curR = i
                curC = j

    print(f'#{tc} {dfs(curR, curC)}')