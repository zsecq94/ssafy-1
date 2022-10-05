import sys; sys.stdin = open('123.txt', 'r')

def bfs(v):
    q = [(v, 0)]
    visited = [0] * (n+1)
    visited[v] = 1
    cnt = 0
    while q:
        a, b = q.pop(0)
        if b <= 2:
            cnt += 1
        for w in tree[a]:
            if not visited[w]:
                visited[w] = 1
                q.append((w, b+1))
    return cnt-1

n = int(input())
m = int(input())

tree = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
# print(tree)
print(bfs(1))