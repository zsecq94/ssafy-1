import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    dump = int(input())
    arr = sorted(map(int, input().split()))

    cnt = 0
    while cnt < dump:
        arr[0] += 1
        arr[-1] -= 1
        arr.sort()
        cnt += 1

    arr.sort()
    print(f'#{tc} {arr[-1] - arr[0]}')






    # for _ in range(dump):
    #     i = arr.index(max(arr))
    #     j = arr.index(min(arr))
    #     arr[i] -= 1
    #     arr[j] += 1
    #
    # print(f'#{tc} {max(arr)-min(arr)}')
