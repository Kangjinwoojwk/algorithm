class Queue:
    def __init__(self):
        self.li = []
        self.front = self.rear = -1
    def push(self, a):
        self.li.append(a)
        self.rear += 1
    def pop(self):
        self.front += 1
        return self.li[self.front]
    def isempty(self):
        return self.rear == self.front
Q = Queue()
for i in range(1, 4):
    Q.push(i)
for i in range(3):
    print(Q.pop())
