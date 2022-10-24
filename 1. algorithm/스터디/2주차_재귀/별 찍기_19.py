import sys; sys.stdin = open('123.txt', 'r')

def f(v, x, y):
    if v == 1:
        arr[a//2][a//2] = '*'
    else:
        for i in range(x, y):
            for j in range(x, y):
                if j == x or i == x or i == y-1 or j == y-1:
                    arr[i][j] = '*'
        f(v-1, x+2, y-2)

N = int(input())
a = 1 + ((N-1)*4)
arr = [[' '] * a for _ in range(a)]
f(N, 0, a)

for i in range(a):
    for j in range(a):
        print(arr[i][j], end='')
    print()