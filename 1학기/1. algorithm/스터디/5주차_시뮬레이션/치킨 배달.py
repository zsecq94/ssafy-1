# import sys; sys.stdin = open('123.txt', 'r')
from itertools import combinations

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
resultV = 99999999

one_lst = []
two_lst = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            one_lst.append((i, j))
        elif arr[i][j] == 2:
            two_lst.append((i, j))

for i in combinations(two_lst, M):
    cnt = 0
    for j in one_lst:
        result = 99999999
        for k in range(M):
            result = min(result, abs(j[0] - i[k][0]) + abs(j[1] - i[k][1]))
        cnt += result
    resultV = min(resultV, cnt)
print(resultV)