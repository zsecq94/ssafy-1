import sys
sys.stdin = open('123.txt', 'r')

primes = [False, False] + [True] * 1000000
def generation(A, B):
    for num in range(2, B+1):
        if primes[num] : # 프라임이 트루면
            for idx in range(num + num, B+1, num):
                primes[idx] = False

T = int(input())
for tc in range(1, T+1):

    D, A, B = map(int, input().split())
    generation(A, B)
    cnt = 0
    for idx in range(A, B + 1):
        if primes[idx] and str(D) in str(idx):
            cnt += 1
    print(f'#{tc} {cnt}')
