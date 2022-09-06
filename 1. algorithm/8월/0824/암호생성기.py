import sys; sys.stdin = open('123.txt', 'r')

def queue(arr):
    q = []
    while not q:
        for i in range(1, 6):
            v = arr.pop(0)
            v = v - i
            if v > 0:
                arr.append(v)
            else:
                arr.append(0)
                while arr:
                    q.append(arr.pop(0))
                break
    return q

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    result1 = queue(arr)
    result = ' '.join(map(str, result1))
    print(f'#{tc} {result}')