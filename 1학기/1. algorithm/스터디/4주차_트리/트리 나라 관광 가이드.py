import sys; sys.stdin = open('123.txt', 'r')

def dfs(v):
    visited[v] = 1
    parent[0] = -1
    for i in tree[v]:
        if not visited[i]:
            parent[i] = v
            visited[i] = 1
            dfs(i)

N = int(input())
arr = list(map(int, input().split()))
tree = [[] for _ in range(max(arr)+1)]
parent = [0] * (N+1)
visited = [0] * (N+1)

a = len(arr)-1
for i in range(a):
    tree[arr[i]].append(arr[i+1])

dfs(0)
for i in range(max(arr)+1):
    print(parent[i], end=' ')