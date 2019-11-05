class EdgeNode:
    def __init__(self, start, finish, weight):
        self.start = start
        self.finish = finish
        self.weight = weight

    def __lt__(self, other):
        return int(self.weight) < int(other.weight)

