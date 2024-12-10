class Stack:
    def __init__(self):
        self.__storage = []
        self.__length = 0

    @property
    def IsEmpty(self):
        return self.__length == 0
    
    @property
    def get_storage(self):
        return self.__storage
    
    def push(self, value):
        self.__storage.append(value)
        self.__length += 1
    
    def pop(self):
        if self.IsEmpty:
            raise ValueError("Storage does not have any items")
        else:
            self.__storage.pop()
            self.__length -= 1

    def peek(self):
        if self.IsEmpty:
            raise ValueError("Storage does not have any items")
        else:
            return self.__storage[-1]
        
s1 = Stack()
s1.push(1)

print(s1.get_storage)
print(s1.peek())

s1.pop()
print(s1.get_storage)

s1.pop()
print(s1.get_storage)
