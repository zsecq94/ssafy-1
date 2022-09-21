import sys; sys.stdin = open('123.txt', 'r')

def f(v, x, y, q):
    if v == 1:
        arr[b//2][b//2] = '*'
        return


    else:
        for i in range(x, y):
            for j in range(x, q):
                if i == x or j == x or i == y-1 or (j == q-1 and i >= x+2) or (i == x+2 and j > q-4):
                    arr[i][j] = '*'
        f(v-1, x+2, y-2, q-2)

N = int(input())
a = 3 + ((N-1)*4)
b = 1 + ((N-1)*4)
if N == 1:
    arr = [[' ']]
else:
    arr = [[' '] * b for _ in range(a)]
f(N, 0, a, b)

for i in range(b):
    for j in range(a):
        print(arr[i][j], end='')
    print()