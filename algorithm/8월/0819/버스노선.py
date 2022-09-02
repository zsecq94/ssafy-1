import sys
sys.stdin = open('123.txt', 'r')

'''
삼성시에 있는 5,000개의 버스 정류장은 관리의 편의를 위해 1에서 5,000까지 번호가 붙어 있다.
그리고 버스 노선은 N개가 있는데, i번째 버스 노선은 번호가 Ai이상이고,
Bi이하인 모든 정류장만을 다니는 버스 노선이다.
P개의 버스 정류장에 대해 각 정류장에 몇 개의 버스 노선이 다니는지 구하는 프로그램을 작성하라.
#1 1 2 2 1 1

1. 1이상 3이하 2. 2이상 5이하
'''

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     cnt = [0] * 5001
#
#     A = [0] * N
#     B = [0] * N
#     for i in range(N):
#         A[i], B[i] = list(map(int,input().split()))
#
#     P = int(input())
#     POS = []
#     for i in range(P):
#         POS.append(int(input()))
#
#     for i in range(N):
#         for i in range(A[i]-1, B[i]):
#             cnt[i] += 1
#
#     for i in range(P):
#         print(cnt[POS[i]], end=' ')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = [0] * 5001
    for _ in range(N):
        A, B = list(map(int,input().split()))
        for i in range(A-1, B):
            cnt[i] += 1
    print(f'#{tc}', end=' ')
    P = int(input())
    for i in range(P):
        pos = int(input())-1
        print(f'{cnt[pos]}', end=' ')
    print()



