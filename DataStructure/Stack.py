# 스택을 구현하는 방법에는 두가지가 있다.
# 1. list로 구현
class StackList(list):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) == 0:
            return -1
        else:
            self.stack.pop()

    def peek(self):
        return self.stack[-1]

# 2. LinkedList로 구현하기
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedList(object):
    def __init__(self):
        self.head = None

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def pop(self):
        if self.head:
            data = self.head.data
            self.head = self.head.next
            return data
        else:
            return -1


    def peek(self):
        if self.head:
            return self.head.data
        return -1

    def is_empty(self):
        if self.head:
            return False
        else:
            return True


if __name__ == "__main__":
    s = StackLinkedList()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.peek())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
