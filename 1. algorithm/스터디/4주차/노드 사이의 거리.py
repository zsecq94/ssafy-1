# import sys; sys.stdin = open('123.txt', 'r')

def bfs(a, b):
    visited = [False] * (N+1)
    visited[a] = True
    q = [(a, 0)]
    while q:
        v, d = q.pop(0)
        if v == b:
            return d

        for i, l in G[v]:
            if not visited[i]:
                visited[i] = True
                q.append((i, d + l))


N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
for i in range(N-1):
    n1, n2, w = map(int, input().split())
    G[n1].append((n2,w))
    G[n2].append((n1,w))

for i in range(M):
    v1, v2 = map(int, input().split())
    print(bfs(v1, v2))