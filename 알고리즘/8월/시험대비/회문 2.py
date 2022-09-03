import sys
sys.stdin = open('123.txt', 'r')

def asd(value):
    if value == value[::-1]:
        return True
    else:
        return False

T = 1
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(20)]
    arr1 = list(zip(*arr))

    # cnt = 0
    # for i in range(100):
    #     for j in range(100):
