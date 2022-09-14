import sys; sys.stdin = open('123.txt', 'r')

def enq(n):
    global last
    last += 1           # 마지막 정점 추가
    heap[last] = n      # 마지막 정점에 key 추가

    c = last
    p = c // 2
    while p and heap[p] > heap[c]:      # 부모가 있고, 부모 > 자식 조건을 만족할때까지 자리 교환
        heap[p], heap[c] = heap[c], heap[p]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    heap = [0] * (len(arr)+1)
    last = 0

    for i in arr:
        enq(i)
    # print(heap)
    a = heap[-1]
    b = heap.index(a) // 2
    result = 0
    while b != 0:
        result += heap[b]
        b //= 2

    print(f'#{tc} {result}')
