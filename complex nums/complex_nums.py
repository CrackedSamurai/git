from parentecies import parentheses
class complex:
    def __init__(self, value):
        self.value = value
        self.__is_num()
    #checks if its a valid number
    def __is_num(self):
        if isinstance(self.value, (int, float)):
            pass
        else:
            print(self.value)
            #raise ValueError("is not num")
    #returns a string version of the number    
    def __str__(self):
        return f"{self.value}i"
    #returns its value
    def return_i(self):
        return self.value
    #addition
    def __add__(self, other):
        if isinstance(other, complex):
            return complex(self.value + other.value)
        else:
            return parentheses(other, self.value)
    def __radd__(self, other):
        return parentheses(other, self.value)
    #subtraction    
    def __sub__(self, other):
        if isinstance(other, complex):
            return complex(self.value - other.value)
        else:
            return parentheses(other, self.value)
    def __rsub__(self, other):
        return parentheses(other, self.value)
    #multiplication    
    def __mul__(self, other):
        if isinstance(other, complex):
            return -(self.value * other.value)
        else:
            return complex(self.value * other)
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

equasion = 4 + complex(5) * (6 - complex(3) - 4 * 4)
print(equasion)