class Node(object):
    def __init__(self, character=None, weight=None, rightChild=None, leftChild=None, parent=None):
        self.character = character  # 字符
        self.parent = parent  # 父节点
        self.rightChild = rightChild  # 右孩子节点
        self.leftChild = leftChild  # 左孩子节点
        self.weight = weight  # 权值

    # 自定义类的比较
    def __lt__(self, other):
        return int(self.weight) < int(other.weight)
