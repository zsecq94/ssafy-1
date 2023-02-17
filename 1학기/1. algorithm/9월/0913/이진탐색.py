import sys; sys.stdin = open('123.txt', 'r')

def asd(v):
    global pos
    if v <= N:
        asd(v*2)
        tree[v] = pos
        pos += 1
        asd(v*2+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    pos = 1

    asd(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')