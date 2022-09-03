import sys; sys.stdin = open('123.txt', 'r')

def bfs(v, N, t):   # v 시작, N 마지막 정점번호, t 찾는정점
    visited = [0] * (N+1)
    Q = []
    Q.append(v)
    visited[v] = 1
    while Q:
        v = Q.pop(0)
        if v == t:
            return visited[99]
            # v에 인접하고 방문 안한 w 인큐. 표시
        for w in adjList[v]:
            if visited[w] == 0:
                Q.append(w)
                visited[w] = visited[v] + 1
    return 0

T = 10
for _ in range(T):
    tc, E = map(int, input().split())
    arr = list(map(int, input().split()))

    adjList = [[] for _ in range(100)]
    for i in range(E):
        a, b = arr[i*2], arr[i*2+1]
        adjList[a].append(b)

    print(bfs(0, 99, 99))  # 시작, 마지막정점, 목표 정점