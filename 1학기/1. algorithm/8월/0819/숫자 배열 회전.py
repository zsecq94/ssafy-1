import sys
sys.stdin = open('123.txt', 'r')

'''
1 2 3
4 5 6
7 8 9
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    des_90 = [[0]*N for _ in range(N)]
    des_180 = [[0]*N for _ in range(N)]
    des_270 = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            des_90[i][j] = arr[N-1-j][i]

    for i in range(N):
        for j in range(N):
            des_180[i][j] = des_90[N-1-j][i]

    for i in range(N):
        for j in range(N):
            des_270[i][j] = des_180[N-1-j][i]

    print(f'#{tc}')
    for i in range(N):
        result1 = ''.join(map(str, des_90[i]))
        result2 = ''.join(map(str, des_180[i]))
        result3 = ''.join(map(str, des_270[i]))
        print(result1, result2, result3)


