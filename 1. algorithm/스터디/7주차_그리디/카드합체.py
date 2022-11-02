import sys; sys.stdin = open('123.txt', 'r')

N, M = map(int, input().split())
arr = list(map(int, input().split()))

V = 0
while V != M:
    arr = sorted(arr)
    A = arr[0] + arr[1]
    arr[0] = A
    arr[1] = A
    V += 1

result = sum(arr)
print(result)