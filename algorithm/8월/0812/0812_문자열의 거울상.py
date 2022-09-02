import sys
sys.stdin = open('123.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    arr = input()
    s = list(arr)
    N = len(arr)
    for i in range(N//2):
        s[i], s[N-1-i] = s[N-1-i], s[i]
    s = ''.join(s)
    s = list(s)

    for j in range(len(s)):
        if s[j] == 'b':
            s[j] = 'd'
        elif s[j] == 'd':
            s[j] = 'b'
        elif s[j] == 'p':
            s[j] = 'q'
        elif s[j] == 'q':
            s[j] = 'p'
    s = ''.join(s)
    print(f'#{tc} {s}')