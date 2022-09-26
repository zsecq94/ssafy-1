import sys; sys.stdin = open('algo1_sample_in.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [0] + list(map(int, input().split())) + [0]

    cnt = 0
    for i in range(0, len(arr)):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            cnt += 1
        elif arr[i] > arr[i-1] and arr[i] == arr[i+1]:
            a = i
            # 같은 높이의 봉우리가 나왔을때 반복
            while True:
                if arr[a] < arr[a+1]:
                    break
                elif arr[a] == arr[a+1]:
                    a += 1
                else:
                    cnt += 1
                    break

    print(f'#{tc} {cnt}')