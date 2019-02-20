import sys
sys.stdin = open('4874.txt', 'r')
sys.stdout = open('4874_out.txt', 'w')


class Stack:
    def __init__(self):
        self.li = []
        self.top = -1

    def push(self, a):
        self.li.append(a)
        self.top += 1

    def pop(self):
        a = self.li[-1]
        self.li = self.li[:-1]
        self.top -= 1
        return a

    def top(self):
        if self.top > -1:
            return self.li[-1]
        return False

    def isempty(self):
        if self.top == -1:
            return True
        return False


T = int(input())
for test_case in range(1, T + 1):
    list_input = input().split()
    list_input = list_input[:-1]
    data = Stack()
    n = len(list_input)
    for i in range(n):
        data.push(list_input[i])
    cal = {'+', '-', '/', '*'}
    cal_stack = Stack()
    i = 0
    get1 = data.pop()
    get2 = ''
    while i < n:
        get2 = data.top()
        if get1 in cal and get2 in cal:
            cal_stack.push(get1)
            get1 = get2
        elif 






        i += 1

