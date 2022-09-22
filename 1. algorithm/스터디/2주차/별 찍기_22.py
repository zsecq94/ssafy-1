# import sys; sys.stdin = open('123.txt', 'r')

def f(v, x, y, q):
    if v == 1:
        arr[a//2][b//2] = '*'
        arr[a//2+1][b//2] = '*'
        return
    # y = i, q = j
    else:
        for i in range(x, y):
            for j in range(x, q):
                if i < a and j < b:
                    if i == x or j == x or i == y-1:
                        arr[i][j] = '*'
                    if (j == q-1 and i >= x+2) or (i == x+2 and j > q-4):
                        arr[i][j] = '*'
        f(v-1, x+2, y-2, q-2)


N = int(input())
a = 3 + ((N-1)*4)
b = 1 + ((N-1)*4)
arr = [[' '] * b for _ in range(a)]

if N == 1:
    print('*')
else:
    f(N, 0, a, b)
    if N == 1:
        print('*')
    else:
        for i in range(a):
            for j in range(b):
                if i == 1:
                    print('*')
                    break
                print(arr[i][j], end='')
            if i != 1:
                print()