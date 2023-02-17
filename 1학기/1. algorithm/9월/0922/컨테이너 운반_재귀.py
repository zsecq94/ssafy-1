import sys; sys.stdin = open('123.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    kg = list(map(int, input().split()))
    t = list(map(int, input().split()))

    print(N, M)
    print(kg)
    print(t)