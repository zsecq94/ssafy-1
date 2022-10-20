import sys; sys.stdin = open('123.txt', 'r')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
minV = 999999999

sumLst = []
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0 and visited[i][j] == False:
            visited[i][j] = True
            visited[j][i] = True
            sumLst.append(arr[i][j] + arr[j][i])

print(sumLst)
A = len(sumLst)
for i in range(A):
    for j in range(A):
        if sumLst[i] - sumLst[j] >= 0 and i != j:
            if minV > sumLst[i] - sumLst[j]:
                minV = sumLst[i] - sumLst[j]

print(minV)