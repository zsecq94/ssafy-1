import sys; sys.stdin = open('123.txt', 'r')

def check(a):
    global result, u
    for i in range(len(a)):
        for j in range(len(a)):
            if i == j:
                continue
            for k in range(len(a)):
                if j == k or i == k:
                    continue
                if (a[i] == a[j]-1 and a[j] == a[k]-1) or (a[i] == a[j] == a[k]):
                    return 1
    return 0


for tc in range(1, int(input())+1):
    arr = list(map(int, input().split()))
    resultA = 0
    resultB = 0
    one = []
    two = []
    u = []
    for i in range(len(arr)):
        if i % 2 == 0:
            one.append(arr[i])
            if len(one) >= 3:
                resultA = check(one)
                if resultA > 0:
                    break

        else:
            two.append(arr[i])
            if len(two) >= 3:
                resultB = check(two)
                if resultB > 0:
                    break

    if resultA > 0:
        print(f'#{tc} 1')
    elif resultB > 0:
        print(f'#{tc} 2')
    elif resultA == 0 and resultB == 0:
        print(f'#{tc} 0')