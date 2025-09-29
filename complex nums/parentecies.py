class parentheses:
    def __init__(self, value_1, value_2):
        if  isinstance(value_1, complex):
            self.number = value_2
            self.comlx = value_1
        else:
            self.number = value_1
            self.comlx = value_2
        self.__is_num()
    #checks if its a valid number
    def __is_num(self):
        if isinstance(self.number, (int, float)):
            pass
        else:
            raise ValueError("is not num")
    #check if nums are in order
    def __in_order(self):
        if self.number > 0:
            pass
        else:
            self.number, self.comlx = self.comlx, self.number
    #returns a string version of the parentheses
    def __str__(self):
        self.__in_order()
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
    #subtraction    
    def __sub__(self, other):
        if isinstance(other, parentheses):
            return parentheses(self.number - other.number, self.comlx - other.comlx)
        elif isinstance(other, complex):
            return parentheses(self.number, self.comlx - other)
        else:
            return parentheses(self.number - other, self.comlx)
    def __rsub__(self, other):
        if isinstance(other, parentheses):
            return parentheses(other.number - self.number, other.comlx - self.comlx)
        elif isinstance(other, complex):
            return parentheses(self.number, other - self.comlx)
        else:
            return parentheses(other - self.number, self.comlx)
    #multiplication    
    def __mul__(self, other):
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