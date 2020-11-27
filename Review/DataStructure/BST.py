import random

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class NodeMgmt:
    def __init__(self, node):
        self.head = node

    def insert(self, value):
        self.current_node = self.head
        while True:
            if self.current_node.value > value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break


    def search(self, value):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.value == value:
                return True
                break
            elif self.current_node.value > value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False

    def delete(self, value):
        self.current_node = self.head
        self.parent = self.head
        searched = False
        while self.current_node != None:
            if self.current_node.value == value:
                searched = True
                break
            elif self.current_node.value > value:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right
        if searched == False:
            return False

        if self.current_node.left == None and self.current_node.right == None:
            if self.parent.value > self.current_node.value:
                self.parent.left = None
            else:
                self.parent.right = None
            del self.current_node

        if self.current_node.left != None and self.current_node.right == None:
            if self.parent.value > self.current_node.value:
                self.parent.left = self.current_node.left
            else:
                self.parent.right = self.current_node.left

        elif self.current_node.right != None and self.current_node.left == None:
            if self.parent.value > self.current_node.value:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.left

        if self.current_node.left != None and self.current_node.right != None:
            if value < self.parent.value:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                while self.change_node.left:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                if self.current_node.right != None:
                    self.change_node_parent.left = self.change_node.right
                else:
                    self.change_node_parent.left = None
                self.parent.left = self.change_node
                self.change_node.left = self.current_node.left
                self.change_node.right = self.current_node.right
            else:
                self.change_node = self.current_node.right
                self.change_node = self.current_node.right
                while self.change_node.left:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                if self.change_node.right:
                    self.change_node_parent.left = self.change_node.right
                else:
                    self.change_node_parent.left = None
                self.parent.right = self.change_node
                self.change_node.left = self.current_node.left
                self.change_node.right = self.current_node.right

bst_nums = set()
while len(bst_nums) != 100:
    bst_nums.add(random.randint(0, 999))

root = Node(500)
bst = NodeMgmt(root)
for num in bst_nums:
    bst.insert(num)

for num in bst_nums:
    if not bst.search(num):
        print("wrong search", num)

delete_num = set()
bst_nums = list(bst_nums)
while len(delete_num) != 10:
    delete_num.add(bst_nums[random.randint(0, 99)])

for num in delete_num:
    if not bst.delete(num):
        print("wrong delete", num)


