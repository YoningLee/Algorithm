prefix = list(input().replace("\n",""))
postfix = '' #출력
stack = [] #스택
for i in prefix:
    if i == '(': #열린 괄호
        stack.append(i)
    elif i in ['+','-']:
        while len(stack)!=0 and stack[-1] in ['*','/','+','-']:
            postfix += stack.pop()
        stack.append(i)
    elif i in ['*','/']:
        while len(stack)!=0 and stack[-1] in ['*','/']:
            postfix += stack.pop()
        stack.append(i)
    elif i == ')':
        while stack[-1] != '(':
            postfix += stack.pop()
        stack.pop()
    else: #문자열인 경우
        postfix += i
while len(stack) != 0:
    postfix += stack.pop()
print(postfix)