class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class NodeMgmt:
    def __init__(self, data):
        self.head= Node(data)

    def add(self, data):
        if self.head == '':
            self.head = Node(data)

        node = self.head
        while node.next:
            node = node.next
        node.next = Node(data)

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next


    def insertHead(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insertAfter(self, prev_node, data):
        if prev_node == None:
            print("error")
            return
        node = Node(data)
        node.next = prev_node.next
        prev_node.next = node

    def delete(self, data):
        if self.head == '':
            print('err')
            return

        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    return
                else:
                    node = node.next


    def search(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next



