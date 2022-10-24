import sys; sys.stdin = open('123.txt', 'r')

def find_area(ix, iy, jx, jy, p):
    global result
    a = arr[ix][jx]
    for i in range(ix, iy):
        for j in range(jx, jy):
            if arr[i][j] != a:
                result.append('(')
                find_area(ix, iy//2, jx, jy//2, p//4)


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

one_cnt = 0
zero_cnt = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            one_cnt += 1
        else:
            zero_cnt += 1
result = []
if one_cnt == N*N:
    print(1)
elif zero_cnt == N*N:
    print(0)
else:
    find_area(0, 4, 0, 4, 16)

print(result)
