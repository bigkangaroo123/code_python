class Stack:
    def __init__(self, storage):
        self.storage = storage
        self.length = len(self.storage)
        self.IsEmpty = None
        if self.length == 0:
            self.IsEmpty = True
        else:
            self.IsEmpty = False

    def IsEmpty(self):
        if len(self.storage) == 0:
            return True
        else:
            return False

    def push(self, item):
        self.storage.append(item)
        self.length += 1
        
    def pop(self):
        self.storage.pop()
        self.length -= 1

    def peek(self):
        return self.storage[-1]

s1 = Stack(["a", "a", "a", "a"])
s1.push("b")
print(s1.peek())

print(s1.storage)
        
s1.push("z")
print(s1.peek())

print(s1.storage)
