class complex:
    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("is not num")
        self.value = value
  
    #returns a string version of the number    
    def __str__(self):
        return f"{self.value}i"
    
    #+
    def __add__(self, other):
        if isinstance(other, parentheses):
            return NotImplemented
        elif isinstance(other, complex):
            return complex(self.value + other.value)
        else:
            return parentheses(other, self)
    __radd__ = __add__

    #-    
    def __sub__(self, other):
        if isinstance(other, parentheses):
            return NotImplemented
        elif isinstance(other, complex):
            return complex(self.value - other.value)
        else:
            return parentheses(-other, self)
    def __rsub__(self, other):
        if isinstance(other, parentheses):
            return NotImplemented
        elif isinstance(other, complex):
            return complex(other.value - self.value)
        self.value = -self.value
        return parentheses(other, self)
    
    #*    
    def __mul__(self, other):
        if isinstance(other, parentheses):
            return NotImplemented
        elif isinstance(other, complex):
            return float(-(self.value * other.value))
        else:
            return complex(self.value * other)
    __rmul__ = __mul__

    #/  
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
        
    #**    
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
                
    #//            
    def __floordiv__(self, other):
        return 1/self.value**other
    
    #comparisons
    #==
    def __eq__(self, other): return self.value == other
    #<
    def __lt__(self, other): return self.value < other
    #<=
    def __le__(self, other): return self.value <= other
    #>
    def __gt__(self, other): return self.value > other
    #>=
    def __ge__(self, other): return self.value >= other

    #abs
    def __abs__(self):
        self.value = abs(self.value)
        return self
    
    #neg
    def __neg__(self):
        return complex(-float(self.value))


class parentheses:
    def __init__(self, value_1, value_2):
        if not isinstance(value_1, (int, float, parentheses, complex)) and isinstance(value_2, (int, float, parentheses, complex)):
            raise ValueError("is not num")
        if not isinstance(value_1, complex):
            self.real = value_1 
            self.imaginary = value_2
        else:
            self.real = value_2
            self.imaginary = value_1
        self.__can_sum()

    #can sum
    def __can_sum(self):
        if self.real == 0:
            return complex(self.imaginary)
        elif self.imaginary == 0:
            return float(self.real)
        elif isinstance(self.real, (int, float)) and isinstance(self.imaginary, (int, float)):
            return float(self.real + self.imaginary)
        elif isinstance(self.real, complex) and isinstance(self.imaginary, complex):
            return complex(self.real + self.imaginary)
        else: return self
    #returns a string version of the parentheses
    def __str__(self):
        self = self.__can_sum()
        if not isinstance(self, parentheses):
            return str(self)
        elif self.real == 0:
            return f"{self.imaginary}"
        elif self.imaginary == 0:
            return f"{self.real}"
        elif self.imaginary > 0:
            return f"({self.real}+{self.imaginary})"
        else:
            return f"({self.real}-{abs(self.imaginary)})"
        
    #+
    def __add__(self, other):
        if isinstance(other, parentheses):
            return parentheses(self.real + other.real, self.imaginary + other.imaginary)
        else:
            return parentheses(self.real + other, self.imaginary)
    __radd__ = __add__
    
    #-    
    def __sub__(self, other):
        if isinstance(other, parentheses):
            return parentheses(self.real - other.real, self.imaginary - other.imaginary)
        else:
            return parentheses(self.real - other, self.imaginary)
    def __rsub__(self, other):
        if isinstance(other, parentheses):
            return parentheses(other.real - self.real, other.imaginary - self.imaginary)
        else:
            return parentheses(other - self.real, self.imaginary)
        
    #*    
    def __mul__(self, other):
        if isinstance(other, parentheses):
            return parentheses(self.real * other.real, self.imaginary * other.real) + parentheses(self.imaginary * other.imaginary, self.real * other.imaginary)
        else:
            return parentheses(self.real * other, self.imaginary * other)
    __rmul__ = __mul__

    #/    
    def __truediv__(self, other):
        if isinstance(other, parentheses):
            numerator  = (self * parentheses(other.real, -other.imaginary)).__can_sum()
            denominator = (other * parentheses(other.real, -other.imaginary)).__can_sum()
            return numerator / denominator
        else:
            return parentheses(self.real / other, self.imaginary / other)
        
    def __rtruediv__(self, other):
        numerator  = other * parentheses(self.real, -self.imaginary).__can_sum()
        denominator = self * parentheses(self.real, -self.imaginary).__can_sum()
        return numerator / denominator

equasion = parentheses(20, complex(15)) / parentheses(10, complex(5)) * 5 + parentheses(2, complex(3)) - 4**2   
print(equasion, type(equasion))