# 1차원 배열

import sys
sys.stdin = open('123.txt', 'r')

N = int(input())
arr = [list(map(int, input().split()))for _ in range(N)]
for i in range(N):
    for j in range(N):
        print(arr[i][j])