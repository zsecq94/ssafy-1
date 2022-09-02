import sys

sys.stdin = open('123.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N):
        maxV = 0
        minV = 101
        for idx in range(i, N):
            if i % 2 == 0:  # i 나누기 2의 나머지가 0이면
                if arr[idx] > maxV:
                    maxV = arr[idx]
                    b = idx
            else:
                if arr[idx] < minV:
                    minV = arr[idx]
                    b = idx

        arr[i], arr[b] = arr[b], arr[i]
    print(f"#{tc}", end=" ")
    print(*arr[0:10])

