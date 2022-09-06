import sys; sys.stdin = open('123.txt', 'r')

# 우 하 좌 상
dr = [0, +1, 0, -1]
dc = [+1, 0, -1, 0]

def asd(curi, curj):
    st = []
    visited = [[False]*N for _ in range(N)]
    # 1. 스택에 시작점을 push, 시작점 방문표시
    st.append((curi, curj))
    visited[curi][curj] = True
    # 2. 스택에 데이터가 있는 동안
    while st:
        curi, curj = st.pop()
        # 3. cur와 연결된 모든 포인트에 대하여 델타
        for i in range(4):
            newi = curi + dr[i]
            newj = curj + dc[i]
            # 4. new 가 이동이 가능하면(선이 연결되어 있으면)
            if '0' <= newi < N and '0' <= newj < N and arr[newi][newj] != '1' and not visited[newi][newj]:
                if arr[newi][newj] == '3':
                    return 1
                st.append((newi, newj))
                visited[newi][newj] = True
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                curi = i
                curj = j

    print(f'#{tc} {asd(curi, curj)}')
