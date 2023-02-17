import sys; sys.stdin = open('123.txt', 'r')

def pat(c):
    result = []
    pat = {
        '0001101': 0, '0011001': 1, '0010011': 2,
        '0111101': 3, '0100011': 4, '0110001': 5,
        '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9
    }
    if c in pat:
        result.append(pat[c])
    else:
        pass
    return result

T= int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]

    b = []
    for i in range(n):
        for j in range(m):
            a = ''.join(map(str, arr[i][j:j+7]))
            if '1' in a and arr[i][j+56] == '1':
                pat(a)
    print(b)
    c = 0
    for i in range(0, 8, 2):
        c += b[i]

    d = 0
    for i in range(1, 8, 2):
        d += b[i]

    result1 = c*3+d
    result = 0
    if result1%10 == 0:
        for i in range(8):
            result += b[i]
        print(f'#{tc} {result}')
    else:
        print(f'#{tc} 0')