import sys; sys.stdin = open('123.txt', 'r')

def asd(arr):
    a = 0

    while a != (M):
        z = arr.pop(0)
        arr.append(z)
        a += 1
    return arr[0]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    print(f'#{tc} {asd(arr)}')