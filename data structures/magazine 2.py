import random

class magazine:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_item = item(value, self.top)
        self.top = new_item
        return self

    def pop(self):
        item = self.top
        self.top = self.top.next
        return item.value

    def peek(self):
        return self.top

    def is_empty(self):
        return self.top is None
    
    def __repr__(self):
        if self.is_empty():
            return "stack: empty"
        current = self.top
        values = []
        while current:
            values.append(current.value)
            current = current.next
        return "stack: " + " -> ".join(map(str, values))


class item:
    def __init__(self, value, next=None):    
        self.value = value
        self.next = next
    def __repr__(self):
        return f"item:{self.value}"

stk = magazine()
for i in range(10):
    i = random.randint(1,20)
    stk.push(i)
print(stk)
print(stk.pop())
print(stk.peek())
print(stk)