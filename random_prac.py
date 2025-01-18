class Person:
    def __init__(self, height, weight):
        self.weight = weight
        self.height = height
    
    def __repr__(self):
        return str(self.height)

p1 = Person(178, 130)
print(p1.__repr__())