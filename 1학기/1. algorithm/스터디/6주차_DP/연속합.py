# import sys; sys.stdin = open('123.txt', 'r')

N = int(input())
arr = list(map(int, input().split()))

for i in range(1, N):
    arr[i] = max(arr[i], arr[i-1] + arr[i])

print(max(arr))