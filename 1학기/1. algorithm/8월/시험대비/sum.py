import sys
sys.stdin = open('123.txt', 'r')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    maxV = 0
    for i in range(100):
        sumV = 0
        for j in range(100):
            sumV += arr[i][j]
        if maxV < sumV:
            maxV = sumV

    for i in range(100):
        sumV = 0
        for j in range(100):
            sumV += arr[j][i]
        if maxV < sumV:
            maxV = sumV

    for i in range(100):
        sumV = 0
        for j in range(100):
            if i == j:
                sumV += arr[i][j]
        if maxV < sumV:
            maxV = sumV

    s = 99
    e = 100
    sumV1 = 0
    for i in range(100):
        for j in range(s, e):
            sumV1 += arr[i][j]
            s -= 1
            e -= 1
        if maxV < sumV1:
            maxV = sumV1
    print(f'#{tc} {maxV}')