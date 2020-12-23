class Stack:
    def __init__(self):
        self.li = []
        self.top = -1

    def isempty(self):
        if self.top == -1:
            return True
        return False

    def push(self, a):
        self.top += 1
        self.li.append(a)

    def pop(self):
        a = self.li[self.top]
        self.li[:] = self.li[:-1]
        self.top -= 1
        return a

    def top(self):
        if self.top == -1:
            return False
        return self.li[self.top]

st = Stack()
for _ in range(3):
    st.push(input())
for _ in range(3):
    a = st.pop()
    print(a)
