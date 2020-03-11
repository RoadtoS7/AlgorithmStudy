# Node 클래스 선언
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


# Single Linked List 선언
class SingleLinkedList(object):
    def __init__(self):
        self.head = None
        self.count = 0

    # Add a new node at the end of the linked list
    def append(self, node):
        if self.head == None:
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node


    def getDataIndex(self, data):
        cur = self.head
        idx = 0

        while cur:
            if cur.data == data:
                return idx
            cur = cur.next
            idx += 1
        return -1

    def insertNodeAtIndex(self, idx, node):
        cur = self.head
        prevn = None
        cur_i = 0

        if idx == 0:
            if self.head:
                nextn = self.head
                self.head = node
                self.head.next = nextn
            else:
                self.head = node
        else:
            while cur_i < idx:
                if cur:
                    prevn = cur
                    cur = cur.next
                    cur_i += 1
                else:
                    break

            if cur_i == idx:
                node.next = cur
                prevn.next = node
            else:
                return -1

    def insertNodeAtData(self, data, node):
        index = self.getDataIndex(data)
        if index != -1:
            self.insertNodeAtIndex(index, node)
        else:
            return -1

    def deleteAtIndex(self, index):
        prevn = None
        curn = self.head
        curi = 0

        if index == 0:
            self.head = curn.next
        else:
            while curi < index:
                if curn.next:
                    prevn = curn
                    curn = curn.next
                    curi += 1
                else:
                    break
            if curi == index:
                prevn.next = curn.next
            else:
                return -1


    def clear(self):
        self.head = None

    def print(self):
        cur = self.head
        string = ""
        while cur:
            string += str(cur.data)
            if cur.next:
                string += "->"
            cur = cur.next


        print(string)


if __name__ == "__main__":
    sl = SingleLinkedList()
    sl.append(Node(1))
    sl.append(Node(2))
    sl.append(Node(3))
    sl.append(Node(5))
    sl.insertNodeAtIndex(3, Node(4))
    sl.print()

    print(sl.getDataIndex(1))
    print(sl.getDataIndex(2))
    print(sl.getDataIndex(3))
    print(sl.getDataIndex(4))
    print(sl.getDataIndex(5))
    sl.insertNodeAtIndex(1, Node(0))
    sl.print()






