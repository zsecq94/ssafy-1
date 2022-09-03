import sys
sys.stdin = open('123.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    box = [0] * N
    for j in range(Q):
        L, R = map(int, input().split())
        for i in range(L-1, R):
            box[i] = j+1

    box = ' '.join(map(str, box))
    print(f'#{tc} {box}')