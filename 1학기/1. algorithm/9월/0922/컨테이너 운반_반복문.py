import sys; sys.stdin = open('123.txt', 'r')


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    kg = list(map(int, input().split()))
    t = list(map(int, input().split()))

    kg, t = sorted(kg), sorted(t)
    kg, t = kg[::-1], t[::-1]

    sumV = 0
    for i in range(M):
        if i < len(kg) and i < len(t):
            if kg[i] <= t[i]:
                sumV += kg[i]
                continue
            else:
                kg.pop(i)
                kg.append(0)
                if kg[i] <= t[i]:
                    sumV += kg[i]
                    continue

    print(f'#{tc} {sumV}')