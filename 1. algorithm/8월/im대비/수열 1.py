import sys; sys.stdin = open('123.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    maxV = 0
    sumV = 0
    for i in range(K):
        maxV += arr[i]
        sumV += arr[i]

    for i in range(N-K):
        sumV -= arr[i]
        sumV += arr[K+i]
        if maxV < sumV:
            maxV = sumV

    print(maxV)