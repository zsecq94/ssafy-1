import sys; sys.stdin = open('123.txt', 'r')

def asd():
    for i in range(len(arr)):
        if arr[i] // M * K - i > 0:
            pass
        else:
            return 'Impossible'
    return 'Possible'

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = sorted(list(map(int, input().split())))

    print(f'#{tc} {asd()}')