class Element:
    def __init__(self, place, weight, value):
        self.id = place
        self.weight = weight
        self.value = value

    def __lt__(self, other):
        return float(self.value/self.weight) < float(other.value/other.weight)


