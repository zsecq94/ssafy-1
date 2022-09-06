import sys
sys.stdin = open('123.txt', 'r')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]+list(map(int, input().split()))+[0] for _ in range(100)]

    for i in range(99, -1, -1):
        for j in range(1, 101):
            if arr[i][j] == 2:
                if arr[i][j-1] == 1:
                    while arr[i][j-1] == 1:
                        arr[i][j-1] = 2
                        j -= 1
                    arr[i-1][j] += 1
                    break
                elif arr[i][j + 1] == 1:
                    while arr[i][j+1] == 1:
                        arr[i][j+1] = 2
                        j += 1
                    arr[i-1][j] += 1
                    break

                elif arr[i-1][j] == 1:
                    arr[i-1][j] += 1
                    break

    for i in range(1):
        for j in range(1, 101):
            if arr[i][j] == 2:
                print(f'#{tc} {j-1}')



