import sys; sys.stdin = open('123.txt', 'r')

def bfs(f, s, g, u, d):
    st = [s]
    while st:
        go = st.pop(0)
        if go == g:
            return visit[go]

        for ngo in (go + u, go - d):
            if 0 < ngo <= f and visit[ngo] == 0:
                st.append(ngo)
                visit[ngo] = visit[go] + 1

    return 'use the stairs'

# f = 전체 층 수, s = 지금 있는 층, g = 도착 층
f, s, g, u, d = map(int, input().split())

visit = [0] * (f+1)
print(bfs(f, s, g, u, d))