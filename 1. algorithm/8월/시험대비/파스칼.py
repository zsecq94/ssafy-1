import sys
sys.stdin = open('123.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    print(f'#{tc}')
    arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(i+1):
            if i == j or j == 0:
                arr[i][j] += 1
            else:
                arr[i][j] = arr[i-1][j] + arr[i-1][j-1]

            print(f'{arr[i][j]}', end=' ')
        print()