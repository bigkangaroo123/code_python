class Circle:
    def __init__(self, radius, diameter):
        self.__radius = radius
        self.__diameter = diameter

    @property
    def radius(self):
        return self.__radius

    @property
    def diameter(self):
        return self.__diameter

    #if u dont write property for both, the one u dont write for, when u print that outside the class, it will give memory location instead of value. so put property

#end of Circle
c1 = Circle(6, 12)
print(c1.radius)
print(c1.diameter)
