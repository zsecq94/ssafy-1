N = 5
lst = [64, 25, 10, 22, 11]

# 0번째 = [0~N-1] 제일 작은 값을 찾아서 0에 위치
# 1번째 = [1~n-1] 제일 작은 값을 찾아서 1에 위치
# N-2 까지 구하면 됨

for phase in range(0, N-1): # 0부터 4까지
    # lst[phase:N-1]중 제일 작은 값의 위치를 찾아
    # minV = lst[phase]
    minP = phase
    for idx in range(phase+1, N):
        if lst[idx] < lst[minP]:
            minP = idx # minV = lst[idx]
    lst[minP], lst[phase] = lst[phase], lst[minP]
    print(lst)