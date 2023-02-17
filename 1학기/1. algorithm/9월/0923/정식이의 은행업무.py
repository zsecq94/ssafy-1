# import sys; sys.stdin = open('123.txt', 'r')

def check(v, t):
    N = len(two)
    M = len(three)
    # 이진수의 i번째가 틀린경우
    for i in range(N):
        # 삼진수의 i번째가 틀린경우
        for j in range(M):
            # b = 이진수의 i번째 데이터를 변경하고
            v = two[:]
            v[i] = (v[i] + 1) % 2
            # t = 삼진수의 j번째 데이터를 변경해서
            for k in [1, 2]:
                t = three[:]
                t[j] = (t[j]+k)%3
                a = ''.join(map(str, v))
                b = ''.join(map(str, t))
                a = int(a, 2)
                b = int(b, 3)
                if a == b:
                    return a
    return -1

for tc in range(1, int(input())+1):
    two = list(map(int, input()))
    three = list(map(int, input()))

    print(f'#{tc} {check(two, three)}')