class Stack:
    def __init__(self):
        self.__storage = []

    @property
    def get_storage(self):
        return self.__storage

    def add_value(self, x):
        self.__storage.append(x)
    
    def remove_val(self, x):
        if x in self.__storage:
            self.__storage.remove(x)
            return f"removed {x} from stack"
        else:
            print("value not found in stack")
    
    def get_last(self):
        return self.__storage[-1]
    
    def get_value(self, x):
        return self.__storage[x]
    
    def set_value(self, index, value):
        if index <= len(self.__storage):
            self.__storage[index] = value
            return f"value set!"
        else:
            return ValueError(f"stack doesnt have {index} values in it")
        
test = Stack()
test.add_value(3)
test.add_value(8)
test.add_value(2)
test.add_value(5)
test.add_value(9)
test.add_value(1)
test.add_value(7)
test.add_value(6)

print(test.get_storage)

test.remove_val(14)

print(test.remove_val(9))
print(test.get_storage)

print(test.get_last())

print(test.set_value(2, 8))
print(test.get_storage)








    