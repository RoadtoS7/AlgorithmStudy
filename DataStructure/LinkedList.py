# 노드는 데이터와 다음 노드를 가리키는 포인터로 구성되어있다.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.count = 0

    def append(self, node):
        if self.head is None:
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def getDataIndex(self, data):
        cur = self.head
        idx = 0
        while cur is not None:
            if cur.data == data:
                return idx
            cur = cur.next
            idx += 1
        return -1

    def inserNodeAtIndex(self, idx, node):
        prev = None
        cur = self.head
        curIdx = 0

        if idx == 0:
            if self.head:
                nextn = self.head
                self.head = node
                node.next = nextn
            else:
                self.head = node

        else:
            while curIdx < idx:
                if cur:
                    prev = cur
                    cur = cur.next
                else:
                    break
                curIdx += 1

            if idx == curIdx:
                prev.next = node
                node.next= cur
            else:
                return -1

    def insertNodeAtData(self, data, node):
        idx = self.getDataIndex(data)
        if 0 <= idx:
            self.inserNodeAtIndex(idx)
        else:
            return -1

    def deleteAtIndex(self, idx):
        prev = None
        cur = self.head

        curIdx = 0

        if idx == 0:
            self.head = cur.next
        else:
            while curIdx < idx:
                if cur:
                    prev = cur
                    cur = cur.next
                else:
                    break
                curIdx += 1
            if curIdx == idx:
                prev.next = cur.next
            else:
                return -1


    def clear(self):
        self.head = Node

    def print(self):
        cur = self.head
        string = ""
        while cur:
            string += str(cur.data)
            if cur.next:
                string += "=>"
            cur = cur.next
        print(string)


if __name__ == "__main__":
    sl = SinglyLinkedList()
    sl.append(Node(1))
    sl.append(Node(2))
    sl.append(Node(3))
    sl.append(Node(5))
    sl.inserNodeAtIndex(3, Node(4))
    sl.print()










