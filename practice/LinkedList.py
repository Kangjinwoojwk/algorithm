class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __del__(self):
        print(self.data, '삭제')


class List:
    def __init__(self):
        self.head = None # 첫 노드 객체
        self.size = 0

    def printlist(self):
        if self.head is None:
            print('빈 리스트입니다.')
            return
        cur = self.head
        print('[', end=' ')
        while cur is not None:
            print(cur.data, end=' ')
            cur = cur.next
        print(']')

    def insertlast(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
        self.size += 1

    def insertfirst(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def deletelast(self):
        if self.head is None:
            print('빈 리스트 입니다.')
        else:
            prev, cur = None, self.head
            while cur.next is not None:
                prev = cur
                cur = cur.next
            if prev is None:
                self.head = self.tail = None
                del cur
            else:
                prev.next = None
                self.tail = prev
                del cur
            self.size -= 1

    def deletefirst(self):
        if self.head is None:
            print('빈 리스트 입니다.')
        else:
            cur = self.head
            if cur.next is None:
                self.head = self.tail = None
            else:
                self.head = self.head.next
            del cur
            self.size -= 1

    def insertAt(self, idx, val):
        if self.head is None:
            self.insertfirst(val)
        elif idx >= self.size:
            self.insertlast(val)
        else:
            prev, cur = None, self.head
            for i in range(idx):
                prev = cur
                cur = cur.next
            if prev is None:
                self.insertfirst(val)
            else:
                node = Node(val)
                node.next = prev.next
                prev.next = node
        self.size += 1

    def deleteAt(self, idx):
        if self.head is None:
            print('빈 리스트입니다.')
        elif idx >= self.size:
            print('인덱스 초과입니다.')
        else:
            prev, cur = None, self.head
            for i in range(idx):
                prev = cur
                cur = cur.next
            prev.next = cur.next
            del cur
            self.size -= 1
