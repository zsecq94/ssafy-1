import sys
sys.stdin = open('123.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    box = [[0] * 10 for _ in range(10)]
    for _ in range(N):
        i1, j1, i2, j2, c = map(int, input().split())

        for i in range(i1, i2+1):
            for j in range(j1, j2+1):
                box[i][j] += c

        cnt = 0
        for i in range(10):
            for j in range(10):
                if box[i][j] == 3:
                    cnt += 1
    print(f'#{tc} {cnt}')
