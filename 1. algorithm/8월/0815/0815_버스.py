import sys
sys.stdin = open('123.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 버스타입, 출발 정류장 번호, 종점 정류장 번호
    for C in range(N):
        arr = list(map(int, input().split()))

        list_a = []
        list_b = []
        list_c = []
        if arr[0] == 1:
            for i in range(arr[1]+1, arr[2]+1):
                list_a.append(i)
        elif arr[0] == 2:
            if arr[1] % 2 == 0:
                for j in range(arr[1]+1, arr[2]+1, 2):
                    list_b.append(j)
            else:
                for q in range(arr[1]+2, arr[2]+2, 2):
                    list_b.append(q)
        # else:
        print(list_a)
        print(list_b)
