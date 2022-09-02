import sys
sys.stdin = open('123.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = input().split()
    arr = input().split()
    M = int(N[1])
    list_a = []

    for i in range(M):
        if arr[i] == 'ZRO':
            arr[i] = 0
        elif arr[i]  == 'ONE':
            arr[i] = 1
        elif arr[i]  == 'TWO':
            arr[i] = 2
        elif arr[i]  == 'THR':
            arr[i] = 3
        elif arr[i]  == 'FOR':
            arr[i] = 4
        elif arr[i]  == 'FIV':
            arr[i] = 5
        elif arr[i]  == 'SIX':
            arr[i] = 6
        elif arr[i]  == 'SVN':
            arr[i] = 7
        elif arr[i]  == 'EGT':
            arr[i] = 8
        else:
            arr[i] = 9

    sort = sorted(arr)

    for j in range(M):
        if sort[j] == 0:
            sort[j] = 'ZRO'
        elif sort[j] == 1:
            sort[j] = 'ONE'
        elif sort[j] == 2:
            sort[j] = 'TWO'
        elif sort[j] == 3:
            sort[j] = 'THR'
        elif sort[j] == 4:
            sort[j] = 'FOR'
        elif sort[j] == 5:
            sort[j] = 'FIV'
        elif sort[j] == 6:
            sort[j] = 'SIX'
        elif sort[j] == 7:
            sort[j] = 'SVN'
        elif sort[j] == 8:
            sort[j] = 'EGT'
        else:
            sort[j] = 'NIN'
    s = ' '.join(sort)
    print(f'{N[0]} {s}')