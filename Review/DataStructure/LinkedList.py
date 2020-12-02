## 특정 노드 삭제
# 삭제하려는 노드의 앞노드의 포인터 = 삭제하려는 노드의 포인터
# del 삭제하려는 노드

# 맨 앞노드 추가
# 삽입하려는 노드의 포인터 = 헤드의 포인터
# 헤드의 포인터 = 삽입하려는 노드의 주소

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def desc(self):
        node = self.head
        while(node):
            print(node.data)
            node = node.next

    def search_node(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            else:
             node.next = node

    def delete(self, data):
        if self.head == '':
            print('warning')
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


        



    def insertHead(self, data):
        new_node = Node(data)
        new_node.next = self.head.next
        self.head = new_node

    def insertNext(self, prev_node, data):
        if prev_node == None:
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    ## 특정 노드 삭제
    # 1. 첫번째 노드 삭제 = head값 바꾸기
    # 2. 가운데 노드 삭제 = 마지막 노드 삭제, 앞노드의 포인터 null로 바꾸기
    # 3. 마지막 노드 삭제 = 중간 노드 삭제, 앞노드의 포인터를 뒤 노드의 주소값으로 바꿔야 한다.
    def delete(self, data):
        if self.head == '':
            print('warning')
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
                    return
                else:
                    node = node.next
