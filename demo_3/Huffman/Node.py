class Node(object):
    def __init__(self, character=None, weight=None, rightChild=None, leftChild=None, parent=None):
        self.character = character
        self.parent = parent
        self.rightChild = rightChild
        self.leftChild = leftChild
        self.weight = weight

    # 自定义类的比较
    def __lt__(self, other):
        return int(self.weight) < int(other.weight)
