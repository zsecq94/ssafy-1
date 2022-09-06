import sys
sys.stdin = open('123.txt', 'r')

def sdq(N):

    for i in range(9):
        cnt = [0] * 9
        for j in range(9):
            cnt[N[i][j] - 1] += 1
            if cnt[N[i][j] - 1] != 1:
                return 0


    for i in range(9):
        cnt = [0] * 9
        for j in range(9):
            cnt[N[j][i]-1] += 1
            if cnt[N[j][i]-1] != 1:
                return 0


    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            cnt = [0] * 9
            for k in range(3):
                for p in range(3):
                    cnt[N[i+k][j+p]-1] += 1
                    if cnt[N[i+k][j+p]-1] != 1:
                        return 0
    return 1

T = int(input())
for tc in range(1, T+1):
    N = [list(map(int, input().split())) for _ in range(9)]

    result = sdq(N)
    print(f'#{tc} {result}')
