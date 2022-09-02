import sys
sys.stdin = open('123.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = int(input().split())

    maxcnt = 0
    cnt = 0
    for i in range(N):
        print(i)
