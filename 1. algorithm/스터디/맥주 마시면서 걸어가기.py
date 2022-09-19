import sys; sys.stdin = open('123.txt', 'r')

def bfs(v):
    st = [v[0]]
    while st:
        nx, ny = st.pop(0)
        if nx == v[-1][0] and ny == v[-1][1]:
            return 'happy'
        else:
            for i in range(n+2):
                if visited[i]:
                    continue
                elif abs(nx - v[i][0]) + abs(ny - v[i][1]) <= 1000:
                    st.append(v[i])
                    visited[i] = 1
    return 'sad'

T = int(input())
for tc in range(1, T+1):
    n = int(input())

    arr = []
    for _ in range(n+2):
        x, y = map(int, input().split())
        arr.append((x, y))
    visited = [0] * (n+2)
    print(bfs(arr))