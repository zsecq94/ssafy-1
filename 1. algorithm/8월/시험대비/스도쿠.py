import sys
sys.stdin = open('123.txt', 'r')

def sdq(arr):
    # 열, 가로 구하기
    for i in range(9):
        # 행
        cnt = [0] * 9
        for j in range(9):
            # cnt가 0~8까지 있기 때문에 arr[i][j]에 1 빼주기
            cnt[arr[i][j]-1] += 1
            # 만약 cnt의 인덱스값 arr[i][j]-1이 1이 아니면 0을 리턴후 종료 0일경우가 아니라 2일 경우를 구하는 코드
            if cnt[arr[i][j]-1] != 1:
                return 0

        cnt = [0] * 9
        # 세로 구하기
        for k in range(9):
            cnt[arr[k][i]-1] += 1
            if cnt[arr[k][i]-1] != 1:
                return 0

        cnt = [0] * 9
        for p in range(9):
            cnt[arr1[i][p]-1] += 1
            if cnt[arr1[i][p]-1] != 1:
                return 0

    return 1


T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    # 3x3 리스트 만들기
    arr1 = []
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            temp = []
            for k in range(3):
                for p in range(3):
                    temp.append(arr[i+k][j+p])
            arr1.append(temp)

    result = sdq(arr)
    print(f'#{tc} {result}')
