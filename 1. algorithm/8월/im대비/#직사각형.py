import sys; sys.stdin = open('123.txt', 'r')

for _ in range(4):
    arr = list(map(int, input().split()))
    a1, a2, b1, b2, c1, c2, d1, d2 = arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7]

    # 점 = c
    if (a1 == d1 and a2 == d2) or (b1 == c1 and b2 == c2) or (a1 == d1 or b2 == c2) or (a2 == d2 and b1 == c1):
        print('c')
    # 선분
    elif b1 == c1 or b2 == c2 or a1 == d1 or a2 == d2:
        print('b')
    # 공통 없음
    elif d2 < a2 or b1 < c1 or b2 < c2 or a1 > d1:
        print('d')
    # 직사각형
    else:
        print('a')