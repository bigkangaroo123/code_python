class Person:
    def __init__(self, name, wealth): #<-- attributes (2 because self doesnt count)
        self.name = name
        self.__wealth = wealth #only exists in the Person class

    def info(self):
        print(f"Person:{self.name} || wealth:{self.wealth}")

    @property
    def wealth(self): #This is the way to access an encapsulated attribute inside its class
        return self.__wealth #get the value, hence the word getter

    #if want to change wealth (usually shouldnt tho):
    @wealth.setter
    def wealth(self, new_value):
        self.__wealth = new_value

#end of class

#THESE ARE OBJECTS: THESE ARE THE INSTANCES OF THE PERSON CLASS:
p1 = Person("Park", 69)
p2 = Person("Marshall", 10000000)
print(p1.wealth)
p1.wealth = 690000
print(p1.wealth)

'''
THINGS TO KNOW FOR THE TEST:
 - identifying a getter
 - identifying a setter
 - purpose of getter and setter
'''
