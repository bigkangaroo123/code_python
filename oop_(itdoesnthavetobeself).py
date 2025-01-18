class Person:
    def __init__(bruh, height, weight):
        bruh.__height = height
        bruh.__weight = weight
    
    @property
    def get_height(bruh):
        return bruh.__height
    
    @property
    def get_weight(bruh):
        return bruh.__weight
    
    def check(bruh, object):
        if object.__weight > bruh.__weight:
            return "yes"
        else:
            return "no"
            
p1 = Person(178, 130)
p2 = Person(162, 121)
print(p1.check(p2))
