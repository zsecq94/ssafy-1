import sys; sys.stdin = open('123.txt', 'r')

T = 10
for tc in range(1, T + 1):
    n1 = int(input())
    arr1 = list(map(int, input().split()))
    n2 = int(input())
    arr2 = list(input().split())

    box = []
    # 명령어의 개수만큼(길이)
    for i in range(len(arr2)):
        if arr2[i] == 'I':
            z = 3

            while z != int(arr2[i + 2]) + 3:
                box.append(int(arr2[i + z]))
                z += 1

            while box:
                arr1.insert(int(arr2[i + 1]), box.pop(-1))

    result = ' '.join(map(str, arr1[:10]))

    print(f'#{tc} {result}')