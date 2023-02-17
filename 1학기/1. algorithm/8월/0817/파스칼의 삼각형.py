import sys
sys.stdin = open('123.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    print(f'#{tc}')
    arr = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(i+1):
            if j == 0 or i == j:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
            print(f'{arr[i][j]}', end=' ')
        print()


# size = 10
# arr = [[0]*size for _ in range(size)]
# for i in range(size):
#     for j in range(i+1):
#         if j == 0 or i == j:
#             arr[i][j] = 1
#         else:
#             arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     print(f'#{tc}')
#     for i in range(N):
#         for j in range(i+1):
#             print(f'{arr[i][j]}', end=' ')
#         print()