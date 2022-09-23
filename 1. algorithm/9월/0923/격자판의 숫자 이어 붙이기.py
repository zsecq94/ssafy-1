import sys; sys.stdin = open('123.txt', 'r')

# def check (x, y):



for tc in range(1, int(input())+1):
    arr = [list(map(int, input().split())) for _ in range(4)]

    print(arr)
    for i in range(4):
        for j in range(4):
            check(i, j)