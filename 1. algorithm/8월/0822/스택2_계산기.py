# step1과 step2 혼동 no

# 중위표기를 후위표기로 바꿔서 return

isp = {'+' : 1, '-' : 1, '*' : 2, '/' : 2, '(' : 0}
icp = {'+' : 1, '-' : 1, '*' : 2, '/' : 2, '(' : 3}

def step1(strV):
    ST = []
    postOrder = []

    for token in strV:
        if token >= 0 or token <= 0:     # token 이 숫자일때:
            postOrder.append(token)
        elif ')':
            while ST[-1] == '(':    # ST에 왼쪽 괄호가 나올때 까지 pop해서 postOrder에 추가(append)
                postOrder.append(ST.pop())

        else:
            if len(ST) == 0:                   # ST에 데이타가 없는 경우
                ST.append(token)            # ST에 token push
            elif isp(ST[-1]) < icp(token):  # St에 token을 append
                ST.append(token)
            else:   # token보다 크거나 같은동아 pop해서 postOrder에 append하고 ST에 token을 push
                while

    while # 스택에 데이타가 있는 동안:
        # pop해서 postOrder에 append

    return postOrder

# 후위표기의 리스트를 받아서 연산 결과를 return
# def step2(postOrder):
#     ST = []
#
#     for token in postOrder:
#         if # token이 숫자일때:
#             # ST에 token push
#         elif '+':
#             # ST에서 두개 pop해서 더하기 연산 결과를 ST에 push
#         elif '*':
#
#         elif '-':
#
#     return ST[-1]

inputV = (6 + 5 * (2 - 8) / 2 )
postOrder = step1(inputV)
# result = step2(postOrder)

print(postOrder)