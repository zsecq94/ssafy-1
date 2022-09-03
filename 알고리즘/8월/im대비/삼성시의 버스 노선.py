import sys; sys.stdin = open('123.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    bus_stop = [0] * 5001
    maxV = 0
    for _ in range(n):
        k, a, b = map(int, input().split())
        bus_stop[a] += 1
        bus_stop[b] += 1

        if k == 1:
            for i in range(a+1, b):
                bus_stop[i] += 1

        elif k == 2:
            for i in range(a+2, b, 2):
                bus_stop[i] += 1

        elif k == 3:
            if a % 2 == 0:
                for i in range(a+1, b):
                    if i % 4 == 0:
                        bus_stop[i] += 1
            else:
                for i in range(a+1, b):
                    if i % 3 == 0 and i % 10 != 0:
                        bus_stop[i] += 1
    for i in bus_stop:
        if maxV < i:
            maxV = i

    print(f'#{tc} {maxV}')