from node import Node

class Tree(object):
    def __init__(self):
        self.root = None

    def addValue(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
        else:
            self.root.addChild(node)

    def search(self, value):
        self.root.search(value)

    def traverse(self):
        self.root.visit()
