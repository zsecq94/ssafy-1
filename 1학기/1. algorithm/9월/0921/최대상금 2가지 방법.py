'''
# 재귀
def solve(k):
    if k == K:
        최대값인지 확인
        return
    for 교환횟수만큼:
        교환
        solve(k+1)
        교환

# 반복문
for k<K:
    for a in arrList(k):
        교환해서 arrList[k] append
'''

'''
import sys; sys.stdin = open('123.txt', 'r')

def f(n, cnt):
    global result
    if n == cnt:
        b = int(''.join(num))
        # print(int(''.join(num)))
        if result < b:
            result = b
    else:
        for i in range(len(num)-1):
            for j in range(i+1, len(num)):
                num[i], num[j] = num[j], num[i]
                f(n+1, cnt)
                num[i], num[j] = num[j], num[i]

for tc in range(1, int(input())+1):
    num, cnt = input().split()
    num = list(num)
    cnt = int(cnt)
    result = 0
    f(0, cnt)
    print(f'#{tc} {result}')
'''
import sys; sys.stdin = open('123.txt', 'r')

def change(q, cnt):
    global maxV
    if q == cnt:
        save = int(''.join(n))
        if maxV < save:
            maxV = save
    else:
        N = len(n)
        for i in range(0, N-1):
            for j in range(i+1, N):
                n[i], n[j] = n[j], n[i]
                save = int(''.join(n))
                if save not in chk[q]:
                    chk[q].append(save)
                    change(q+1, cnt)
                n[i], n[j] = n[j], n[i]


for tc in range(1, int(input())+1):
    n, cnt = input().split(); n = list(n); cnt = int(cnt)
    chk = [[] for _ in range(cnt)]
    maxV = 0
    change(0, cnt)
    print(f'#{tc} {maxV}')
