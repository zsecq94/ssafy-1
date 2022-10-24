import sys; sys.stdin = open('123.txt', 'r')

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

