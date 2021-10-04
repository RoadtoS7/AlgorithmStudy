class Node:
    def __init__(self, key):
        self.key = key
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, word):
        cur = self.head

        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Node(ch)
            cur = cur.children[ch]

        cur.children['*'] = True

    def search(self, word):
        cur = self.head

        for ch in word:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]

        return '*' in cur.children


trie = Trie()
trie.insert("kim")
trie.insert("kimm")
print(trie.search("ki"))
print(trie.search("kimmm"))

