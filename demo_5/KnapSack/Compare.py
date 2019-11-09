# 用来做比较
class Compare:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

    def __lt__(self, other):
        return float(self.value/self.weight) > float(other.value/other.weight)
