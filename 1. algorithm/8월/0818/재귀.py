
G = [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [3, 6]]
visited = [0] * 8

def dfs(v):
    s = []
    s.append(v)
    visited[v] = True
    while s:
        v = s.pop(-1)
        print(v, end=' ')
        for w in G[v]:
            if not visited[w]:
                s.append(w)
                visited[w] = True

# def dfsr(v):
#     visited[v] = True
#     print(v, end=' ')
#     for w in G[v]:
#         if not visited[w]:
#             dfsr(w)

dfs(1)