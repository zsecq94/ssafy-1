import sys; sys.stdin = open('123.txt', 'r')

def asd():
    result = []

    for i in S:
        if i < 0:
            return 'ERROR'
    Scnt = sum(S)-1

    for i in D:
        if i < 0:
            return 'ERROR'
    Dcnt = sum(D)-1

    for i in H:
        if i < 0:
            return 'ERROR'
    Hcnt = sum(H)-1

    for i in C:
        if i < 0:
            return 'ERROR'
    Ccnt = sum(C)-1

    result.append(Scnt)
    result.append(Dcnt)
    result.append(Hcnt)
    result.append(Ccnt)

    return ' '.join(map(str, result))

T = int(input())
for tc in range(1, T+1):
    t = input()
    A = []
    B = []
    for i in range(0, len(t), 3):
        A.append(t[i])
        B.append(int(t[i+1:i+3]))

    S = [1] * 14
    D = [1] * 14
    H = [1] * 14
    C = [1] * 14

    for i in range(len(A)):
        if A[i] == 'S':
            S[B[i]] -= 1
        elif A[i] == 'D':
            D[B[i]] -= 1
        elif A[i] == 'H':
            H[B[i]] -= 1
        elif A[i] == 'C':
            C[B[i]] -= 1
    print('#{} {}'.format(tc, asd()))

    # print(f'#{tc} {asd()}')