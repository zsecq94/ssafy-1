import sys; sys.stdin = open('123.txt', 'r')

def asd(N):
    st = []
    for i in N:
        if str.isdigit(i):
            st.append(int(i))
        elif i == '.':
            if len(st) == 1:
                return st.pop()
            else:
                return 'error'
        else:
            if len(st) > 1:
                if i == '+':
                    op2 = st.pop()
                    op1 = st.pop()
                    st.append(op1 + op2)
                elif i == '*':
                    op2 = st.pop()
                    op1 = st.pop()
                    st.append(op1 * op2)
                elif i == '-':
                    op2 = st.pop()
                    op1 = st.pop()
                    st.append(op1 - op2)
                elif i == '/':
                    op2 = st.pop()
                    op1 = st.pop()
                    st.append(op1 // op2)
            else:
                return 'error'

T = int(input())
for tc in range(1, T+1):
    N = input().split()

    result = asd(N)
    print(f'#{tc} {result}')