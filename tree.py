from node import Node


class Tree(object):
    def __init__(self):
        self.root = None

    def add_value(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
        else:
            self.root.add_child(node)

    def search(self, value):
        self.root.search(value)

    def traverse(self):
        self.root.visit()
