import sys
sys.stdin = open('123.txt', 'r')

def pal(value):
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
            if pal(arr[i][j:j+M]):
                print(f'#{tc} {arr[i][j:j+M]}')

            str_a = ''
            # arr을 M만큼 str_a에 넣고 바로 pal로 넘김
            for k in range(M):
                str_a += arr[j + k][i]
            if pal(str_a):
                print(f'#{tc} {str_a}')
