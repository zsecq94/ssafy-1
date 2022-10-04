for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    result = []
    for i in arr:
        if i % 4 == 0:
            result.append(i)
        elif i % 6 == 0:
            result.append(i)
        elif i % 7 == 0:
            result.append(i)
        elif i % 9 == 0:
            result.append(i)
        elif i % 11 == 0:
            result.append(i)

    while sum(result) > M:
        result.pop()
    print(f'#{tc} {sum(result)}')