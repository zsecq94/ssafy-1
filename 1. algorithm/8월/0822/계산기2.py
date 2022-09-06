import sys; sys.stdin = open('123.txt', 'r')

isp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
icp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3}

def asd(exp):
    st = []
    result = []
    for i in exp:
        # i가 숫자면
        if '0' <= i <= '9':
            result.append(i)
        # i가 숫자가 아니면
        else:
            # st안에 값이 있으면
            if st:
                # 스택의 마지막 값이 icp[i] 이상이면
                while icp[i] <= isp[st[-1]]:
                    result.append(st.pop())
                    # st이 비어있으면
                    if not st:
                        break
            st.append(i)
    # st이 남아있으면 result에 pop함
    while st:
        result.append(st.pop())
    return ''.join(result)


def dsa(exp):
    result = []
    for i in exp:
        # i가 숫자면 숫자형으로 바꿔서 result에 append
        if '0' <= i <= '9':
            result.append(int(i))
        # i가 숫자가 아니면
        else:
            # 계산하기 쉽게 2부터 pop
            op2 = result.pop()
            op1 = result.pop()
            if i == '+':
                result.append(op1 + op2)
            elif i == '*':
                result.append(op1 * op2)
    return result.pop()


T = 10
for tc in range(1, T + 1):
    N = int(input())
    arr = input()

    arr1 = asd(arr)
    print(f'#{tc} {dsa(arr1)}')