from sys import stdin
input = stdin.readline
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class NodeMgmt:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
            return
        self.current_node = self.head
        while True:
            if data[0] < self.current_node.data[0]:
                if self.current_node.left is not None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(data)
                    break
            elif data[0] > self.current_node.data[0]:
                if self.current_node.right is not None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(data)
                    break

    def search(self, data):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.number[0] < data:
                self.current_node = self.current_node.right
            elif self.current_node.number[0] > data:
                self.current_node = self.current_node.left
            else:
                return self.current_node


    def find_higher_one(self, score):
        higher_ones = set()
        node = self.search(score)

        need_visit = list()
        if node.left:
            need_visit.append(node.left)

        while need_visit:
            cur_node = need_visit.pop(0)
            higher_ones.add(cur_node.number[1])
            if cur_node.left:
                need_visit.append(cur_node.left)
            if cur_node.right:
                need_visit.append(cur_node.right)
        return higher_ones

T = int(input())


for _ in range(T):
    N = int(input())
    document_scores = NodeMgmt()
    interview_scores = NodeMgmt()
    candidate_scores = dict()
    result = 0

    for i in range(N):
        document, interview = map(int, input().split())
        candidate_scores[i] = (document, interview)
        document_scores.insert((document, i))
        interview_scores.insert((interview, i))

    for i in range(N):
        document, interview = candidate_scores[i]
        document_higher = document_scores.find_higher_one(document)
        interview_higher = interview_scores.find_higher_one(interview)
        if len(document_higher.intersection(interview_higher)) == 0:
            print(document_higher)
            print(interview_higher)
            result += 1

    print(result)






