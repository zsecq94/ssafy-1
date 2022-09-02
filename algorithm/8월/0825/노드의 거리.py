import sys; sys.stdin = open('123.txt', 'r')

def queue(S):
    q = [S]
    visit[S] = 1

    while q:
        Z = q.pop(0)
        for i in gra[Z]:
            if visit[i] == 0:
                q.append(i)
                visit[i] = visit[Z] + 1
    if visit[G] == 0:
        return 0
    else:
        return visit[G] - 1

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    gra = [[] for _ in range(V+1)]

    for i in range(E):
        q1, q2 = map(int, input().split())
        gra[q1].append(q2)
        gra[q2].append(q1)

    S, G = map(int, input().split())
    visit = [0] * (V + 1)
    print(f'#{tc} {queue(S)}')
