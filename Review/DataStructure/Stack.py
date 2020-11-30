class StackList(object):
    def __init__(self):
        self.data = []

    def push(self, data):
        self.data.append(data)

    def pop(self):
        if len(self.data) == 0:
            return -1
        else:
            return self.data.pop()

    def peek(self):
        if len(self.data) == 0:
            return -1
        else:
            return self.data[-1]


class Node:
    def __init__(self, data):
        self.data = data
        self.head = None


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
            data = self.head.data
            return data
        else:
            return -1

    def print(self):
        cur = self.head
        string = ""
        while cur:
            string += str(cur.data)
            if cur.next:
                string += "=>"
            cur = cur.next

if __name__ == "__main__":
    stack = StackLinkedList()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.peek()) # 3
    print(stack.pop()) # 3
    print(stack.pop()) # 2
    print(stack.pop()) # 1
    print(stack.pop()) # -1