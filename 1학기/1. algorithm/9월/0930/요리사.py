import sys; sys.stdin = open('123.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    foodA = []
    foodB = []
    # foodA구하기
    for i in range(1, 1 << N):
        a = []
        for j in range(N):
            if i & (1 << j):
                a.append(j)
        if len(a) == N//2:
            foodA.append(a)
    # foodB구하기
    for i in foodA:
        b = []
        for j in range(N):
            if j not in i:
                b.append(j)
        foodB.append(b)
    food_A = foodA[:len(foodA)//2]
    food_B = foodB[:len(foodB)//2]

    print(food_A, food_B)
    for i in range(len(food_B)):
        for j in range(len(food_B)):
            print(arr[i][j])