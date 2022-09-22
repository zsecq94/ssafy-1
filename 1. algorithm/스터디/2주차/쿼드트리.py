import sys; sys.stdin = open('123.txt', 'r')

def find_area(v, a):
    for i in range(v):
        for j in range(a):
            print(arr[i][j])


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

zero_cnt = 0
one_cnt = 0

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            one_cnt += 1
        else:
            zero_cnt += 1

if zero_cnt or one_cnt:
    if zero_cnt == 0:
        print(1)
    elif one_cnt == 0:
        print(0)
else:
    a = N / 2
    find_area(0, a)

