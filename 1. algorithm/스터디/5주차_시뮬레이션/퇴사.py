# import sys; sys.stdin = open('123.txt', 'r')

N = int(input())
day = []
money = []
dp = [0] * (N + 1)
maxV = 0

for i in range(N):
    a, b = map(int, input().split())
    day.append(a)
    money.append(b)

for i in range(N-1, -1, -1):
    time = day[i] + i
    if time <= N:
        dp[i] = max(money[i] + dp[time], maxV)
        maxV = dp[i]
    else:
        dp[i] = maxV
print(maxV)