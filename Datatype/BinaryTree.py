class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return self.data

class Tree:
    def __init__(self):
        self.root = None

    def preorderTraversal(self, node):
        print(node.data, end='')
        if not node.left == None: self.preorderTraversal(node.left)
        if not node.right == None: self.preorderTraversal(node.right)

    def inorderTraversal(self, node):
        if not node.left == None: self.inorderTraversal(node.left)
        print(node.data, end ='')
        if not node.right == None: self.inorderTraversal(node.right)

    def postorderTraversal(self, node):
        if not node.left == None: self.postorderTraversal(node.left)
        print(node.data, end ='')
        if not node.right == None: self.postorderTraversal(node.right)

    def makeRoot(self, node, leftNode, rightNode):
        if self.root == None:
            self.root = node
        node.left = leftNode
        node.right = rightNode

if __name__  == "__main__":
    node = []
    node.append(Node('-'))
    node.append(Node('*'))
    node.append(Node('/'))
    node.append(Node('A'))
    node.append(Node('B'))
    node.append(Node('C'))
    node.append(Node('D'))

    tree = Tree()
    for i in range(int(len(node)/2)):
        tree.makeRoot(node[i], node[i*2 + 1], node[i*2 + 2 ])

    print('전위 순회:', end = '')
    tree.preorderTraversal(tree.root)
    print('\n중위 순회:', end='')
    tree.inorderTraversal(tree.root)
    print('\n후위 순회:', end='')
    tree.postorderTraversal(tree.root)