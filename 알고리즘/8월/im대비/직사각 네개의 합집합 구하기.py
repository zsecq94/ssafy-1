import sys; sys.stdin = open('123.txt', 'r')

arr = [[0] * 101 for _ in range(101)]

for i in range(4):
    ii, jj, xx, yy = map(int,input().split())

    for k in range(ii+1, xx+1):
        for kk in range(jj+1, yy+1):
            if arr[k][kk] == 0:
                arr[k][kk] = 1

cnt = 0
for i in range(101):
    for j in range(101):
        if arr[i][j] == 1:
            cnt += 1
print(cnt)