import sys; sys.stdin = open('123.txt', 'r')

num = {
        '0001101': 0, '0011001': 1, '0010011': 2,
        '0111101': 3, '0100011': 4, '0110001': 5,
        '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9
    }

def find_end(N, M):
    for i in range(N):
        for j in range(M - 1, 54, -1):
            if arr[i][j] == '1':
                return i, j - 55

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    si, sj = find_end(N, M)
    code = [0] * 8
    for i in range(8):
        code[i] = num[arr[si][sj:sj+7]]
        sj += 7

    c = 0
    for i in range(0, 8, 2):
        c += code[i]

    d = 0
    for i in range(1, 8, 2):
        d += code[i]

    result1 = c*3+d
    result = 0
    if result1%10 == 0:
        for i in range(8):
            result += code[i]
        print(f'#{tc} {result}')
    else:
        print(f'#{tc} 0')