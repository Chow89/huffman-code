class BinaryTree(object):

    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.value)+" "+str(self.left)+" "+str(self.right)

    def insert(self, value, route):
        if route[0] == '0':
            if len(route) == 1:
                self.left = BinaryTree(value, None, None)
            else:
                self.left.insert(value, route[1:])
        else:
            if len(route) == 1:
                self.right = BinaryTree(value, None, None)
            else:
                self.right.insert(value, route[1:])