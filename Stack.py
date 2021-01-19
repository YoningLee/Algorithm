class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


prec = {
    '*': 3,
    '/': 3,
    '+': 2,
    '-': 2,
    '(': 1,
}


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    opStack = ArrayStack()
    postfixList = []

    for token in tokenList:
        if type(token) is int:  # 정수
            postfixList.append(token)
        elif token == '(':  # 열린 괄호
            opStack.push(token)
            continue
        elif token == ')':  # 닫힌 괄호
            while opStack.peek() != '(':
                postfixList.append(opStack.pop())
            opStack.pop()
        else:  # 연산자
            while opStack.size() > 0 and prec[opStack.peek()] >= prec[token]:
                postfixList.append(opStack.pop())
            opStack.push(token)
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return postfixList


def postfixEval(tokenList):
    valStack = ArrayStack()

    for c in tokenList:
        valStack.push(c)
        if c in prec:
            B = valStack.pop()  # 연산자
            C = valStack.pop()  # 피연산자
            A = valStack.pop()  # 피연산자
            if B is '+':
                valStack.push(A + C)
            elif B is '-':
                valStack.push(A - C)
            elif B is '*':
                valStack.push(A * C)
            else:
                valStack.push(A / C)

    return valStack.pop()


def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val
