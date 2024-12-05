class Animal:  #this class will be the main daddy of our inheritance
    def __init__(self, name):
        self.name = name

    #create these methods for every single class:
        
    def __str__(self): #creates string equiviland
        return f"Animal: {self.name}"

    def __repr__(self): #this makes it printable
        return self.__str__()

    def sound(self):
        return "urf!"
    
    #if u create one of the methods, create the other (str and repr)

#end of Animal

class Dog(Animal): #Animal class is Dog class's parent
    def info(self):
        return "I AM ACTUALLY A DOG"

    def sound(self):
        return "woof"

#this is single inheritance because class Animal only has 1 caller

a1 = Animal("Seal")
d1 = Dog("Marshall")
print(a1.sound())
print(d1.sound())


#the messiness of inheritance: 
