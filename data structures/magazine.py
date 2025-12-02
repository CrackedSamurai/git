import random

class magazine:
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
        print(self)
        return self

    def pop(self):
        item = self.data[self.used_slots - 1]
        self.data[self.used_slots - 1] = None
        self.used_slots -= 1
        return item

    def peek(self):
        return self.data[self.used_slots - 1]
    
    def __free_space(self):
        if self.used_slots >= self.slots:
            return False
        return True
    def __resize(self):
        new_data = [None]*(self.slots+10)
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

    
mag = magazine()
for i in range(24):
    i = random.randint(1,30)
    mag.push(i)
print(mag.pop())
print(mag.peek())
print(mag)