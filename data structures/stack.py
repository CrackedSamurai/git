class stack:
    def __init__(self):
        self.data = [None]*10
        self.slots = len(self.data)
        self.used_slots = 0

    def push(self, value):
        if self.__free_space():
            self.data[self.used_slots] = value
        else:
            self.__resize()
            self.data[self.used_slots] = value
        self.used_slots += 1
        self.slots = len(self.data)
        return self

    def pop(self):
        
        self.slots = len(self.data)
    def peek(self, index):
        return self.data[index]
    
    def __free_space(self):
        if self.used_slots >= self.slots:
            return False
        return True
    def __resize(self):
        new_data = [None]*(self.slots*2)
        for i in range(self.used_slots):
            new_data[i] = self.data[i]
        self.data = new_data
        self.slots = len(self.data)
        return self
    def __len__(self):
        return len(self.data)
    def __repr__(self):
        if self.used_slots == 0:
            return "magazine: empty"
        return f"magazine:{self.data}, slots{self.slots}, used_slots:{self.used_slots}"

class item:
    def __init__(self, value):    
        self.value = value
        self.next = None
    def __repr__(self):
        return f"item:{self.value}"

stk = stack()
stk.push("first")
stk.push("second")
stk.push("third")
stk.pop()
print(stk.peek(0))
print(stk)