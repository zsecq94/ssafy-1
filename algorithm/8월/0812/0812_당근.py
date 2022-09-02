import sys
sys.stdin = open('123.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    C = list(map(int, input().split()))
    print(N)
    print(C)