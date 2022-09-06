import sys
sys.stdin = open('123.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    maxV = 0
    minV = 0
    for i in range(1):
        maxV = arr[i]
        minV = arr[i]

    for i in range(N):
        if maxV < arr[i]:
            maxV = arr[i]
        if minV > arr[i]:
            minV = arr[i]
    print(f'#{tc} {maxV - minV}')