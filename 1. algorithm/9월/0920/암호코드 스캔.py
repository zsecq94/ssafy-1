import sys; sys.stdin = open('123.txt', 'r')
'''
1. 16진수를 2진수로 만든다.
newARR = [] # N * (M*4)
2. 제일 오른쪽 끝에 있는 1을 찾는다 > 1의 개수를 세고 > 0의 개수를 세고 > 1의 갯수를 센다. (코드 하나를 구하기)
'''
hex = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110',
    '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101',
    'E': '1110', 'F': '1111',
}
code_pat = {
    211: 0, 221: 1, 122: 2, 411: 3, 132: 4,
    231: 5, 114: 6, 312: 7, 213: 8, 112: 9,
}

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    newArr = [''] * N
    cnt = 0
    for i in range(N):
        for j in range(M):
            newArr[i] += hex[arr[i][j]]

    for row in range(1, N):
        if not '1' in newArr[row]:
            continue

        j = M*4-1
        while j >= 56:
            if newArr[row][j] == '1' and newArr[row-1][j] == '0':
                result = [0] * 8
                for i in range(8):
                    a = [0] * 3
                    while newArr[row][j] == '1':
                        a[2] += 1; j -= 1

                    while newArr[row][j] == '0':
                        a[1] += 1; j -= 1

                    while newArr[row][j] == '1':
                        a[0] += 1; j -= 1

                    while newArr[row][j] == '0':
                        j -= 1

                    k = min(a)
                    result[i] += code_pat[a[0]//k * 100 + a[1]//k * 10 + a[2]//k]
                last = result[::-1]
                asd = (last[0] + last[2] + last[4] + last[6]) * 3 + last[1] + last[3] + last[5] + last[7]
                if asd % 10 == 0:
                    cnt += sum(last)

            else:
                j -= 1

    print(f'#{tc} {cnt}')


