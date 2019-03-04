import sys
sys.stdin = open('4874.txt', 'r')
sys.stdout = open('4874_out.txt', 'w')


def sol(ptr):
    n = len(list_input)
    cal = {'+', '-', '*', '/'}
    if n == 1:
        return
    if list_input[ptr + 2] in cal:
        if list_input[ptr + 2] == '*':
            list_input[ptr] = str(int(list_input[ptr]) * int(list_input[ptr + 1]))
        elif list_input[ptr + 2] == '+':
            list_input[ptr] = str(int(list_input[ptr]) + int(list_input[ptr + 1]))
        elif list_input[ptr + 2] == '-':
            list_input[ptr] = str(int(list_input[ptr]) - int(list_input[ptr + 1]))
        elif list_input[ptr + 2] == '/':
            list_input[ptr] = str(int(list_input[ptr]) // int(list_input[ptr + 1]))
        list_input[:] = list_input[:ptr + 1] + list_input[ptr+3:]
        return sol(ptr - 1)
    return sol(ptr + 1)


T = int(input())
for test_case in range(1, T + 1):
    list_input = input().split()
    list_input = list_input[:-1]
    cal = {'+', '-', '*', '/'}
    n = len(list_input)
    count = [0, 0]
    for i in range(n):
        if list_input[i] in cal:
            count[1] += 1
        else:
            count[0] += 1
    if (count[0] - 1) != count[1]:
        list_input = ['error']
    sol(0)
    print('#{} {}'.format(test_case, list_input[0]))



