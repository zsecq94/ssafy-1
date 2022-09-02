import sys
sys.stdin = open('123.txt', 'r')

T = 10
for tc in range(1, T+1):
    t = int(input())
    arr = [[0]+list(map(int, input().split()))+[0] for _ in range(100)]

    for i in range(100, 0, -1):
        for j in range(100, 0, -1):
            if arr[i-1][j] == 2:
                if arr[i-1][j-1] == 1:  # 왼
                    arr[i-1][j-1] = arr[i-1][j]
                elif arr[i-1][j+1] == 1:
                    while True:
                        if arr[i - 1][j + 1] == 0:
                            arr[i - 2][j] = arr[i - 1][j]
                            break
                        arr[i-1][j+1] = arr[i-1][j]
                        j += 1
                else:  # 위
                    arr[i-2][j] = arr[i-1][j]

    point = 0
    for i in range(1):
        for j in range(1):
            point = arr[i].index(2)-1
    print(f'#{tc} {point}')