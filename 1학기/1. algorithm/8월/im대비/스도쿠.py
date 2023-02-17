import sys; sys.stdin = open('123.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    cnt = [[0]*9 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            arr[i][j]

    # print(cnt)

    # cnt = [[0]*9 for _ in range(9)]
    # for i in range(9):
    #     for j in range(9):
    #         cnt[j][i] += 1
    #
    # for i in range(0, 6, 3):
    #     for j in range(0, 6, 3):
    #         for ii in range(3):
    #             for jj in range(3):
