import sys; sys.stdin = open('123.txt', 'r')

n, k = map(int, input().split())
arr = []
for i in range(1, n+1):
    arr.append(i)

result = []
a = -1
while len(result) != n:
    a += k
    if a > len(arr):
        a -= n
        result.append(arr[a])
        arr.pop(a)
    else:
        result.append(arr[a])
        arr.pop(a)