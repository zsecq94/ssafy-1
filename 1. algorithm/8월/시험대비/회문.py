import sys
sys.stdin = open('123.txt', 'r')

def asd(value):
    if value == value[::-1]:
        return True
    else:
        return False

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    for i in range(N):
        for j in range(N-M+1):
            if asd(arr[i][j:j+M]):
                print(f'#{tc} {arr[i][j:j+M]}')

            hi = ''
            for k in range(M):
                hi += arr[j + k][i]
            if asd(hi):
                print(f'#{tc} {hi}')
