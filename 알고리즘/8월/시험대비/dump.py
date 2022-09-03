import sys
sys.stdin = open('123.txt', 'r')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = sorted(list(map(int, input().split())))

    for i in range(N):
        arr[-1] -= 1
        arr[0] += 1
        arr = sorted(arr)

    maxV = 0
    minV = arr[0]
    for j in range(100):
        if maxV < arr[j]:
            maxV = arr[j]
        if minV > arr[j]:
            minV = arr[j]
    print(f'#{tc} {maxV - minV}')