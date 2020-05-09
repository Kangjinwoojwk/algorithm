# 연산자 우선순위를 정할 수 있을 때 최대 상금은?

def solution(expression):
    answer = [0]
    numbers = ['']
    operators = []
    for i in expression:
        if '0'<= i <='9':
            numbers[-1] += i
        else:
            operators.append(i)
            numbers.append('')
    operator = list(set(operators))
    operatorN = [0] * len(operator)
    visitOperator = [True] * len(operator)
    def cal():
        numbersDoOperate = [int(i) for i in numbers]
        operatorsDoOper = [i for i in operators]
        for i in range(len(operator)):
            oper = operator[operatorN.index(i)]
            while oper in operatorsDoOper:
                ptr = operatorsDoOper.index(oper)
                if oper == '*':
                    numbersDoOperate[ptr] *= numbersDoOperate[ptr + 1]
                elif oper == '+':
                    numbersDoOperate[ptr] += numbersDoOperate[ptr + 1]
                elif oper == '-':
                    numbersDoOperate[ptr] -= numbersDoOperate[ptr + 1]
                numbersDoOperate = numbersDoOperate[:ptr + 1] + numbersDoOperate[ptr + 2:]
                operatorsDoOper = operatorsDoOper[:ptr] + operatorsDoOper[ptr + 1:]
        if abs(numbersDoOperate[0]) >  answer[0]:
            answer[0] = abs(numbersDoOperate[0])
    def sol(n):
        if n == len(operator):
            cal()
            return
        for i in range(len(operator)):
            if visitOperator[i]:
                visitOperator[i] = False
                operatorN[i] = n
                sol(n + 1)
                visitOperator[i] = True
    sol(0)
    return answer[0]