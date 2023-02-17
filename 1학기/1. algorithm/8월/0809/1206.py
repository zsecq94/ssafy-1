import sys
sys.stdin = open("input.txt", "r")

T = 10
for tc in range(1, T+1):
    a = int(input())
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    maxV = 0
    for i in range(N):
        sumV = 0
        for j in range(N):
            sumV += arr[i][j]
        if maxV < sumV:
            maxV = sumV

    for i in range(N):
        sumV = 0
        for j in range(N):
            sumV += arr[j][i]
        if maxV < sumV:
            maxV = sumV

    sumV = 0
    for i in range(N):
        sumV += arr[i][i]
    if maxV < sumV:
        maxV = sumV

    sumV = 0
    for i in range(N):
        sumV += arr[i][N-1-i]
    if maxV < sumV:
        maxV = sumV

    # print()

    print(maxV)