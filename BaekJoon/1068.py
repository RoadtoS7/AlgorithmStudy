class Node:
    def __init__(self):
        self.child = []

    def setChild(self, node):
        self.child.append(node)

    def deleteChild(self, node):
        self.child.remove(node)

def preorder(node):
    global cnt
    if len(node.child) == 0:
        cnt += 1
    for i in node.child:
        preorder(tree[i])

cnt = 0
N = int(input())
tree = [Node() for _ in range(N)]
parent = list(map(int, input().split()))

for i in range(N):
    if parent[i] != -1:
        tree[parent[i]].setChild(i)

if N != 1:
    i = int(input())
    if parent[i] == -1:
        cnt = 0
    else:
        tree[parent[i]].deleteChild(i)
        preorder(tree[parent.index(-1)])

print(cnt)

