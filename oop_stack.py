class Stack:
    def __init__(self):
        self.__storage = []
        self.length = len(self.__storage)
        self.__IsEmpty = True

    @property
    def IsEmpty(self):
        return self.__IsEmpty

    def get_storage(self):
        return self.__storage

    def push(self, item):
        self.__storage.append(item)
        self.length += 1
        self.__IsEmpty = False 
        
    def pop(self):
        if self.length > 0:
            self.length -= 1

        else:
            raise ValueError("There are no values in storage")

        if self.length == 0:
            self.__IsEmpty == True
        else:
            self.__IsEmpty == False

    def peek(self):
        if self.length > 0:
            return self.__storage[-1]
        else:
            raise ValueError("The stack is empty")

test = Stack()
print(f"is the stack empty?: {test.IsEmpty}")

test.push(2)
test.push(1)
test.push(5)

print(f"current storage: {test.get_storage()}")
print(test.peek())
print(f"last value: {test.pop()}")
print(f"is the stack empty now?: {test.IsEmpty}")
print(f"current storage: {test.get_storage()}")

