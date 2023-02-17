import sys; sys.stdin = open('123.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    cnt = [0] * 1001
    for asd in range(N):
        No, A, B = map(int, input().split())
        if No == 1:
            for i in range(A, B+1):
                cnt[i] += 1
        elif No == 2:
            cnt[A] += 1
            cnt[B] += 1
            for i in range(A, B+1, 2):
                if i == A:
                    cnt[i] += 0
                elif i == B:
                    cnt[i] += 0
                else:
                    cnt[i] += 1
        elif No == 3:
            cnt[A] += 1
            cnt[B] += 1
            if A % 2 == 0:
                for i in range(A, B+1):
                    if i % 4 == 0:
                        if i == A:
                            cnt[i] += 0
                        elif i == B:
                            cnt[i] += 0
                        else:
                            cnt[i] += 1
            else:
                for i in range(A, B+1):
                    if i % 3 == 0 and i % 10 != 0:
                        if i == A:
                            cnt[i] += 0
                        elif i == B:
                            cnt[i] += 0
                        else:
                            cnt[i] += 1

    result = 0
    for k in cnt:
        if result < k:
            result = k

    print(f'#{tc} {result}')