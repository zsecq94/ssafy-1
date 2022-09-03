import sys; sys.stdin = open('123.txt', 'r')

bg = [list(map(int, input().split())) for _ in range(5)]
arr = [list(map(int, input().split())) for _ in range(5)]

print(len(arr))