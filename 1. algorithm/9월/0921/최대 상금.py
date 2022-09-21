import sys; sys.stdin = open('123.txt', 'r')

def f(n, cnt):
    global result
    if n == cnt:
        tmp = int(''.join(num))
        if result < tmp:
            result = tmp
    else:
        for i in range(len(num)-1):
            for j in range(i+1, len(num)):
                num[i], num[j] = num[j], num[i]
                tmp = int(''.join(num))
                if tmp not in u[n]:     # 교환한 숫자가 죽복체크 리스트에 없으면 추가하고 넘어감, 있으면 그냥 넘어감
                    u[n].append(tmp)
                    f(n+1, cnt)
                num[i], num[j] = num[j], num[i]


for tc in range(1, int(input())+1):
    num, cnt = input().split()
    num = list(num)
    cnt = int(cnt)
    result = 0
    u = [[] for _ in range(cnt)]     # 중복 노드 체크
    f(0, cnt)
    print(f'#{tc} {result}')