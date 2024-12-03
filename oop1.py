import random

class Dog:
    def __init__(self, name, breed, age):
        self.name = name #.name is just making the name of the Dog accessible. it can be anything
        self.breed = breed
        self.age = age
        self.pee()
        self.bark()

    def pee(self):
        need_to_pee = ["yes", "no"]
        choice = random.choice(need_to_pee)
        if choice == "yes":
            print(f"{self.name} NEEDS TO PEE")
        elif choice == "no":
            print(f"{self.name} is allg")

        
    def bark(self): #self is required, its a keyword that makes attributes within a class
        print("BARK BARK BARK")

#end of class Dog

dog1 = Dog("Marshall", "westie", "2")
print(f"The dog is a {dog1.breed} named {dog1.name}")
