import sys; sys.stdin = open('123.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, P = list(map(int, input().split()))

    list_a = []
    while len(list_a) < P - 1:
        list_a.append(N // P)
    list_a.append(N // P + N % P)

    for i in range(max(list_a) - min(list_a) - 1):
        list_a[-1] -= 1
        list_a[i] += 1

    maxV = list_a[0]
    for i in range(1, len(list_a)):
        maxV *= list_a[i]

    print(f'#{tc} {maxV}')