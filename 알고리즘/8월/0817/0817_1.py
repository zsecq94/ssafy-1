
# push
def push(item, size):
    global top
    top += 1
    if top == size:
        print('overflow!')
    else:
        stack[top] = item

size = 10
stack = [0] * size
top = -1

push(10, size)
top += 1
stack[top] = 20
print(stack)
print(top)

'''
def pop(): # 파라미터 값 없으면 마지막 꺼내옴
    if len(s) == 0: # 꺼낼거 없으면 underflow
        return print('underflow')
    else:
        return s.pop(-1)
'''

def pop():
    global top
    if top == -1:
        print('underflow')
    else:
        top -= 1
        return stack[top+1]

print(pop())

if top > -1:
    top -= 1
    print(stack[top+1])