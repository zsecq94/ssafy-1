import sys
sys.stdin = open('123.txt', 'r')

isp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
icp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3}

def asd(arr):
    ST = []
    result = []
    for i in arr:
        # 피연산자일때
        if '0' <= i <= '9':
            result.append(i)
        # 오른쪽 괄호
        elif i == ')':
            # ST에 (가 나올때 까지 ST을 pop해서 result에 추가(append)
            while ST[-1] != '(':
                result.append(ST.pop())
            # 왼쪽 만나면
            ST.pop()
        # 연산자, 왼쪽괄호
        else:
            if ST:
                while icp[i] <= isp[ST[-1]]:
                    result.append(ST.pop())
                    if not ST:
                        break
            ST.append(i)
    # 스택에 남아 있으면
    while ST:
        result.append(ST.pop())
    return ''.join(result)

def calc(exp):
    ST = []
    for token in exp:
        # 피연산자 push
        if '0' <= token <= '9':
            ST.append(int(token))
        # 연산자
        else:
            op2 = ST.pop()
            op1 = ST.pop()
            if token == '+':
                ST.append(op1 + op2)
            elif token == '-':
                ST.append(op1 - op2)
            elif token == '*':
                ST.append(op1 * op2)
            elif token == '/':
                ST.append(op1 / op2)

    return ST.pop()

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = input()

    result1 = asd(arr)
    print(f'#{tc} {calc(result1)}')