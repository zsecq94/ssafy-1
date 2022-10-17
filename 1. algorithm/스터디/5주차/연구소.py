import sys; sys.stdin = open('123.txt', 'r')
from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

print(arr)