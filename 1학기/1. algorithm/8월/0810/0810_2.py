N = 3  # 행의 크기
M = 4  # 열의 크기
# N개의 원소를 갖는 0으로 초기화된 1차원배열
arr1 = [0]*N

# 크기가 NxM 이고 0으로 초기화된 2차원 배열
arr2 = [[0]*M for _ in range(N)]
# print(arr2)

# 크기가 동일하지 않아도 가능
arr3 = [[1], [2, 3], [3, 4, 5]]
# print(arr3)

arr4 = [['-']*M for _ in range(N)]
print(arr4)

