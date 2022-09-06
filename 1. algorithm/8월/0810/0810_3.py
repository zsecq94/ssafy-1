'''
# 배열의 합
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

sumV = 0
for i in range(N):
    for j in range(len(arr)):
        sumV += arr[i][j]
    print(sumV)
'''

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

maxV = 0
for i in range(N):
    rs = 0  # 행의 합
    for j in range(len(arr)):  # i행의 j열에 접근
        rs += arr[j][i]
    if maxV < rs:
        maxV = rs
print(maxV)