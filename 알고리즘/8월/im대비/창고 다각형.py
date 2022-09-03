import sys; sys.stdin = open('123.txt', 'r')

N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]

arr = [[0] * 20 for _ in range(20)]

for i in range(20):
    for j in range(20):
        if arr[L[0]][L[1]] == 0:
            arr[L[0]][L[1]] = 1