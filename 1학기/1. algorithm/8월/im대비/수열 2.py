import sys; sys.stdin = open('123.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    sumM = 0
    sumV = 0
    minV = 0
    for i in range(N-1):
        if arr[i] <= arr[i+1]:
            sumV += 1
            if sumM < sumV:
                sumM = sumV
        elif arr[i] > arr[i+1]:
            sumV = 0
        if arr[i] >= arr[i+1]:
            minV += 1
            if sumM < minV:
                sumM = minV
        elif arr[i] < arr[i+1]:
            minV = 0
    print(sumM + 1)