import sys
sys.stdin = open('123.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = list(input())

    st = []
    for i in range(len(N)):
        if N[i] == '(' or N[i] == '{':
            st.append(N[i])
        elif len(st)>0 and st[-1] == '(' and N[i] == '}':
            break
        elif len(st)>0 and st[-1] == '{' and N[i] == ')':
            break
        elif len(st)>0 and st[-1] == '(' and N[i] == ')':
            st.pop()
        elif len(st)>0 and st[-1] == '{' and N[i] == '}':
            st.pop()
        elif not st and N[i] == ')':
            st.append(N[i])
            break
        elif not st and N[i] == '}':
            st.append(N[i])
            break

    if len(st) == 0:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')


    # arr = []
    # size = len(arr)
    # cnt1 = 0
    # cnt2 = 0
    # cnt3 = 0
    # cnt4 = 0
    #
    # for i in N:
    #     if i == '(':
    #         arr.append(i)
    #         cnt1 += 1
    #     elif i == ')':
    #         arr.append(i)
    #         cnt2 += 1
    #     elif i == '{':
    #         arr.append(i)
    #         cnt3 += 1
    #     elif i == '}':
    #         arr.append(i)
    #         cnt4 += 1
    #
    # if cnt1 == cnt2 and cnt3 == cnt4:
    #     if arr[0] == '(' and arr[-1] == ')':
    #         print(f'#{tc} 1')
    #     elif arr[0] == '{' and arr[-1] == '}':
    #         print(f'#{tc} 1')
    # else:
    #     print(f'#{tc} 0')

