import sys; sys.stdin = open('123.txt', 'r')

def bfs(v):
    # st에 집 좌표를 저장
    st = [v[0]]
    while st:
        nx, ny = st.pop(0)
        if nx == v[-1][0] and ny == v[-1][1]:
            return 'happy'
        else:
            # 방문처리 포문
            for i in range(n+2):
                # 방문하지 않았고, 맨해튼 거리가 1000 이하면
                if visited[i] == 0 and abs(nx - v[i][0]) + abs(ny - v[i][1]) <= 1000:
                    st.append(v[i])
                    visited[i] = 1
    return 'sad'


T = int(input())
for tc in range(1, T+1):
    n = int(input())

    # 모든 좌표를 입력받아서 arr에 저장
    arr = []
    for _ in range(n+2):
        x, y = map(int, input().split())
        arr.append((x, y))

    # 방문 처리를 위한 visited
    visited = [0] * (n+2)
    print(bfs(arr))