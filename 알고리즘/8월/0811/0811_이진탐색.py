import sys

sys.stdin = open('123.txt', 'r')
# 목표 page수를 받아서 count를 return 한다
def find(P, key):
    l = 1
    r = P
    cnt = 0
    while l <= r:
        c = int((l+r)/2)
        cnt += 1
        if c == key:
            return cnt
        elif key > c:
            l = c
        elif key < c:
            r = c

T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())

    a1 = find(P, A)
    a2 = find(P, B)
    if a1 > a2:
        print(f"#{tc} B")
    elif a1 < a2:
        print(f"#{tc} A")
    else:
        print(f"#{tc} 0")

