import sys; sys.stdin = open('123.txt', 'r')

# 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    p = [0] * (N+1)
    cnt = [0] * (N+1)

    for i in range(1, N+1):
        p[i] = i

    for i in range(0, len(arr), 2):
        union_parent(p, arr[i], arr[i+1])

