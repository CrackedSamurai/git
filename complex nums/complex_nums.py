class complex:
    def __init__(self, value):
        self.value = value
        self.__is_num()
    #checks if its a valid number
    def __is_num(self):
        if isinstance(self.value, (int, float)):
            pass
        else:
            raise ValueError("is not num")
    #returns a string version of the number    
    def __str__(self):
        return f"{self.value}i"
    #returns its value
    def return_i(self):
        return self.value
    #addition
    def __add__(self, other):
        if isinstance(other, parentheses):
            return NotImplemented
        elif isinstance(other, complex):
            return complex(self.value + other.value)
        else:
            return parentheses(other, self.value)
    def __radd__(self, other):
        if isinstance(other, parentheses):
            return NotImplemented
        return parentheses(other, self.value)
    #subtraction    
    def __sub__(self, other):
        if isinstance(other, parentheses):
            return NotImplemented
        elif isinstance(other, complex):
            return complex(self.value - other.value)
        else:
            return parentheses(other, self.value)
    def __rsub__(self, other):
        if isinstance(other, parentheses):
            return NotImplemented
        elif isinstance(other, complex):
            return complex(other.value - self.value)
        return parentheses(other, self.value)
    #multiplication    
    def __mul__(self, other):
        if isinstance(other, parentheses):
            return NotImplemented
        elif isinstance(other, complex):
            return -(self.value * other.value)
        else:
            return complex(self.value * other)
    def __rmul__(self, other):
        if isinstance(other, parentheses):
            return NotImplemented
        elif isinstance(other, complex):
            return -(self.value * other.value)
        else:
            return complex(self.value * other)
    #division    
    def __truediv__(self, other):
        if isinstance(other, parentheses):
            return NotImplemented
        elif isinstance(other, complex):
            return (self.value / other.value)
        else:
            return complex(self.value / other)
    def __rtruediv__(self, other):
        if isinstance(other, parentheses):
            return NotImplemented
        elif isinstance(other, complex):
            return(other.value / self.value)
        else:
            return complex(other / self.value)
    #power    
    def __pow__(self, other):
        if isinstance(other, complex):
            raise ValueError("not yet built in function: complex ** complex")
        else:
            if other % 2 == 0:
                if other % 4 == 0:  
                    return self.value
                else:
                    return -self.value
            else:
                if (other-1) % 4 == 0:
                    return complex(self.value)
                else: 
                    return complex(-self.value)
    #floor            
    def __floordiv__(self, other):
        return 1/self.value**other
    #<
    def __lt__(self, other):
        return self.value < other
    #<=
    def __le__(self, other):
        return self.value <= other
    #>
    def __gt__(self, other):
        return self.value > other
    #>=
    def __ge__(self, other):
        return self.value >= other

class parentheses:
    def __init__(self, value_1, value_2):
        if  isinstance(value_1, complex):
            self.number = value_2
            self.comlx = value_1
        else:
            self.number = value_1
            self.comlx = value_2
        #self.__is_num()
        self.__can_sum()
    #checks if its a valid number
    def __is_num(self):
        if isinstance([self.number, self.comlx], (int, float, complex, parentheses)):
            pass
        else:
            raise ValueError("is not num")
    #can sum
    def __can_sum(self):
        if isinstance([self.number, self.comlx], (int, float,)):
            return self.number + self.comlx
        elif isinstance([self.number, self.comlx], complex):
            return self.number + self.comlx
    #returns a string version of the parentheses
    def __str__(self):
        if self.comlx >= 0:
            return f"({self.number}+{self.comlx})"
        else:
            return f"({self.number}-{abs(self.comlx)})"
    #addition
    def __add__(self, other):
        if isinstance(other, parentheses):
            return parentheses(self.number + other.number, self.comlx + other.comlx)
        elif isinstance(other, complex):
            return parentheses(self.number, self.comlx + other)
        else:
            return parentheses(self.number + other, self.comlx)
    def __radd__(self, other):
        if isinstance(other, parentheses):
            return parentheses(self.number + other.number, self.comlx + other.comlx)
        elif isinstance(other, complex):
            return parentheses(self.number, self.comlx + other)
        else:
            return parentheses(self.number + other, self.comlx)
    #subtraction    
    def __sub__(self, other):
        if isinstance(other, parentheses):
            return parentheses(self.number - other.number, self.comlx - other.comlx)
        elif isinstance(other, complex):
            print("complex")
            return parentheses(self.number, self.comlx - other)
        else:
            print("num")
            return parentheses(self.number - other, self.comlx)
    def __rsub__(self, other):
        if isinstance(other, parentheses):
            return parentheses(other.number - self.number, other.comlx - self.comlx)
        elif isinstance(other, complex):
            return parentheses(self.number, other - self.comlx)
        else:
            return parentheses(other - self.number, self.comlx)
    #multiplication    
    def __rmul__(self, other):
        if isinstance(other, parentheses):
            return parentheses(parentheses(self.number * other.number, self.comlx * other.number) + parentheses(self.number * other.comlx, self.comlx * other.comlx))
        else:
            return parentheses(self.number * other, self.comlx * other)
    def __rmul__(self, other):
        if isinstance(other, parentheses):
            return parentheses(parentheses(self.number * other.number, self.comlx * other.number) + parentheses(self.number * other.comlx, self.comlx * other.comlx))
        else:
            return parentheses(self.number * other, self.comlx * other)
    #division    
    def __truediv__(self, other):
        if isinstance(other, complex):
            return (self.value / other.value)
        else:
            return complex(self.value / other)
    def __rtruediv__(self, other):
        if isinstance(other, complex):
            return(other.value / self.value)
        else:
            return complex(other / self.value)
    #power    
    def __pow__(self, other):
        if isinstance(other, complex):
            raise ValueError("not yet built in function: complex ** complex")
        else:
            if other % 2 == 0:
                if other % 4 == 0:  
                    return self.value
                else:
                    return -self.value
            else:
                if (other-1) % 4 == 0:
                    return complex(self.value)
                else: 
                    return complex(-self.value)
    #floor            
    def __floordiv__(self, other):
        return 1/self.value**other

equasion = parentheses(4, complex(5)) - complex(3)
print(equasion)