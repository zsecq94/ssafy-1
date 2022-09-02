import sys
sys.stdin = open('123.txt', 'r')


def dfs(S):
    stack = [S]
    visited[S] = 1

    while stack:
        S = stack.pop()

        for w in graph[S]:
            if visited[w] == 0:
                stack.append(w)
                visited[w] = 1

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]

    for i in range(E):
        idx, val = map(int, input().split())
        graph[idx].append(val)
    S, G = map(int, input().split())

    visited = [0] * (V+1)

    dfs(S)
    if visited[G] == 1:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')


