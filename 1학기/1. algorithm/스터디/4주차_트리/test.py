import sys; sys.stdin = open('123.txt', 'r')

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

# 노드 방문 여부와 순서 확인
visited = [0 for i in range(n + 1)]

# 각 연결된 노드를 표현
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

print(graph)