import sys
sys.stdin = open('123.txt', 'r')

def dfs(S):
    st = [S]
    visit[S] = 1

    while st:
        v = st.pop()

        for w in gra[v]:           #v랑 연결된 노드를 하나씩 w에
            if visit[w]==0:         #방문 안했으면 :
                st.append(w)
                visit[w] = 1

for tc in range(1,11):
    T, N = map(int, input().split())
    arr = list(map(int, input().split()))
    gra = [[] for _ in range(101)]

    for i in range(0, N*2, 2):
        idx, val = arr[i], arr[i+1]
        gra[idx].append(val)

    visit = [0] * (100)
    S, G = 0, 99
    dfs(S)
    if visit[G] == 1:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')