class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def addChild(self, node):
        if (node.value < self.value):
            if self.left is None:
                self.left = node
            else:
                self.left.addChild(node)
        elif (node.value > self.value):
            if self.right is None:
                self.right = node
            else:
                self.right.addChild(node)

    def search(self, value):
        if self.value == value:
            print("FOUND " + str(value))
        elif value < self.value and self.left is not None:
            self.left.search(value)
        elif value > self.value and self.right is not None:
            self.right.search(value)
        else:
            print(str(value) + " not found")

    def visit(self):
        if self.left is not None:
            self.left.visit()

        print(self.value)

        if self.right is not None:
            self.right.visit()
