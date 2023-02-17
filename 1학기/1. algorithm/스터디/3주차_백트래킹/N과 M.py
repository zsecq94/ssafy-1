import sys; sys.stdin = open('123.txt', 'r')

N, M = map(int, input().split())
arr = list(map(int, input().split()))

print(N, M)
print(arr)