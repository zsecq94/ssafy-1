# import sys; sys.stdin = open('123.txt', 'r')

for tc in range(1, int(input())+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))

    result = 999 * 999
    for i in range(1 << len(arr)):
        sumV = 0
        for j in range(len(arr)):
            if i & (1 << j):
                sumV += arr[j]
        sumV = sumV - B
        if sumV >= 0 and sumV < result:
            result = sumV
    print(f'#{tc} {result}')