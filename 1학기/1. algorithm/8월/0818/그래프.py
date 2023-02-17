import sys
sys.stdin = open('123.txt', 'r')

def dfs(S):
    st = [S]
    visit[S] = 1
    while st:
        S = st.pop()

        for w in gra[S]:
            if visit[w] == 0:
                st.append(w)
                visit[w] = 1

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    gra = [[] for _ in range(V+1)]

    for i in range(E):
        idx, val = map(int, input().split())
        gra[idx].append(val)
    S, G = map(int, input().split())

    visit = [0] * (V+1)
    dfs(S)
    if visit[G] == 1:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')


