class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class DoublyLinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, node):
        if self.head:
            cur = self.head
            while cur.right:
                cur = cur.right
            cur.right = node
            node.left = cur
        else:
            self.head = node

    def insertNodeAtIndex(self, idx, node):
        prev = None
        cur = self.head
        curIdx = 0

        if idx == 0:
            nextn = cur
            self.head = node
            node.right = nextn
            node.left = self.head
        else:
            while curIdx < idx:
                if cur:
                    prev = cur
                    cur = cur.right
                    curIdx +=1
                else:
                    break
            if curIdx == idx:
                prev.right = node
                node.left = prev
                node.right = cur
                if cur:
                    cur.left = node
            else:
                return -1

    def getDataIndex(self, data):
        cur = self.head
        curIdx = 0

        while cur.right:
            if cur.data == data:
                return curIdx
            cur = cur.right
            curIdx += 1
        return -1

    def inserNodeAtDaat(self, data, node):
        index = self.getDataIndex(data)
        if index >= 0:
            self.insertNodeAtIndex(index, node)
        else:
            return -1

    def deleteAtIndex(self, idx):
        cur = self.head
        prev = None
        curIdx = 0

        if idx == 0:
            if self.head:
                self.head = self.head.right
            else:
                return -1
        else:
            while curIdx < idx:
                if cur.right:
                    prev = cur
                    cur = cur.right
                    curIdx += 1
                else:
                    break
            if curIdx == idx:
                if cur.right:
                    cur.right.left = prev
                prev.right = cur.right
            else:
                return -1

    def print(self):
        cur = self.head
        string = ""
        prev = None
        while cur:
            string += str(cur.data)
            if cur.right:
                string += "<->"
            cur = cur.right
        print(string)

if __name__ == "__main__":
    dl = DoublyLinkedList()
    dl.append(Node(1))
    dl.append(Node(2))
    dl.append(Node(3))
    dl.append(Node(4))
    dl.append(Node(6))
    dl.print()
    dl.insertNodeAtIndex(4, Node(7))
    dl.print()
    dl.insertNodeAtIndex(6, Node(5))
    dl.print()
    dl.deleteAtIndex(6)
    dl.print()




