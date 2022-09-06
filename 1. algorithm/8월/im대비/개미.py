import sys; sys.stdin = open('123.txt', 'r')

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

arr =[[0] * w for _ in range(h)]

