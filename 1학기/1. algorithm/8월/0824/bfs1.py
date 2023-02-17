import sys; sys.stdin = open('123.txt', 'r')
# v = 시작정점, N : 마지막 정점
def bfs(v, N):
    # visited 생성
    visited = [0] * (N+1)
    # Q 생성
    Q = []
    # 시작점 인큐
    Q.append(v)
    # 시작점 방문 처리
    visited[v] = 1
    # 큐가 비어있지 않으면
    while Q:
        # 디큐
        v = Q.pop(0)
        # visit(v)
        print(v)
        # 인접하고 방문하지 않은(인큐되지 않은) 정점 w가 있으면
        for w in adjList[v]:
            if visited[w] == 0:
                Q.append(w)
                visited[w] = visited[v] + 1


V, E = map(int, input().split())
N = V + 1
adjList = [[] for _ in range(N)]
for _ in range(E):
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)

    print(bfs(0, 8))