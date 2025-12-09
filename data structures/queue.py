import random

class queue():
    def __init__(self):
        self.first = None
        self.last = None

    def push(self, value):
        new_item = item(value)
        if not self.first:
            self.first = new_item
            self.last = new_item
        else:
            self.last.next = new_item
            self.last = new_item
        return self
    
    def pop(self):
        if not self.first:
            return None
        if self.first == self.last:
            popped_item = self.first
            self.first = None
            self.last = None
            return popped_item
        current = self.first
        self.first = current.next
        return current
    
    def peek(self):
        if not self.first:
            return None
        return self.first
    
    def is_empty(self):
        if not self.first:
            return True

    def __repr__(self):
        if self.is_empty():
            return "queue: empty"
        current = self.first
        values = []
        while current:
            values.append(current.value)
            current = current.next
        return "queue: " + " -> ".join(map(str, values))
    
class item():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    def __repr__(self):
        return f"item:{self.value}"

stk = queue()
for i in range(10):
    i = random.randint(1,20)
    stk.push(i)
    print(stk)
print(stk.pop())
print(stk)
print(stk.peek())
