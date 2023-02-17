
def solve(k, r, c, d):
    if d == 3 and r == result[0][0] and c == result[0][1]:

        return

    if r하고 c가 범위를 벗어나거나 같은 디저트면:
        return

    newR, newC = ?
    solve(k+1, newR, newC, d)
    d = (d+1) % 4
    newR, newC = ?
    solve(k+1, newR, newC, d)

for r in range(N):
    for c in range(N):
        result = [(r, c)]
        deserLst = [arr[r][c]]
        solve(1, r, c, 0)