import sys; sys.stdin = open('123.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    arr = [-1] + list(input())
    cnt = 0
    z = 1
    while arr.count('Y') > 0:
        if arr[z] == 'Y':
            for i in range(z, len(arr), z):
                if arr[i] == 'Y':
                    arr[i] = 'N'
                else:
                    arr[i] = 'Y'
            cnt += 1
        z += 1
    if arr.count('Y') == 0:
        print(cnt)
    else:
        print('-1')