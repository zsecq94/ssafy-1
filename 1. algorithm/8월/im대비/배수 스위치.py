import sys; sys.stdin = open('123.txt', 'r')

def asd(arr):
    cnt = 0
    Z = 1

    while True:
        Y = 0
        N = 0
        for i in range(1, len(arr)):
            if arr[i] == 'Y':
                Y += 1
            else:
                N += 1
        if Y == 0:
            return cnt
        else:
            if arr[Z] == 'Y':
                for i in range(Z, len(arr), Z):
                    if arr[i] == 'Y':
                        arr[i] = 'N'
                    else:
                        arr[i] = 'Y'
                cnt += 1
            Z += 1

T = int(input())
for tc in range(1, T+1):
    arr = [-1] + list(input())

    print(asd(arr))

