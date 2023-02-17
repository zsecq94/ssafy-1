import sys
sys.stdin = open('123.txt', 'r')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    cnt = 0
    for i in range(2, N-2):
        maxV = 0
        if arr[i] > arr[i-1] and arr[i] > arr[i-2] and arr[i] > arr[i+1] and arr[i] > arr[i+2]:
            if maxV < arr[i-1]:
                maxV = arr[i-1]
            if maxV < arr[i-2]:
                maxV = arr[i-2]
            if maxV < arr[i+1]:
                maxV = arr[i+1]
            if maxV < arr[i+2]:
                maxV = arr[i+2]
            cnt += arr[i] - maxV
    print(f'#{tc} {cnt}')
