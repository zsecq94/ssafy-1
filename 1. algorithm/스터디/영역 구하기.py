import sys; sys.stdin = open('123.txt', 'r')

m, n, k = map(int, input().split())
arr = [[0] * n for _ in range(m)]

for _ in range(k):
    a = list(map(int, input().split()))

    for i in range(a[1], a[3]):
        for j in range(a[0], a[2]):
            if arr[i][j] == 0:
                arr[i][j] = 1
cnt = 0
result = []
for i in range(m):
    for j in range(n):
        if arr[i][j] == 0:
            arr[i][j] = 2
print(arr)

