import sys
sys.stdin = open('123.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = list(input())

    size = len(N)
    st = []
    for i in range(size):
        if len(st) == 0:
            st.append(N[i])
            continue
        if N[i] != st[-1]:
            st.append(N[i])
        else:
            st.pop()
    print(f'#{tc} {len(st)}')


