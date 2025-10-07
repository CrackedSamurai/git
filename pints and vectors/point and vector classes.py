class point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}; {self.y})"
    def __add__(self, other):
        if isinstance(other, vector):
            return point(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Operand must be a vector")
    __radd__ = __add__

    def __sub__(self, other):
        if isinstance(other, vector):
            return point(self.x - other.x, self.y - other.y)
        elif isinstance(other, point):
            return vector(self.x - other.x, self.y - other.y)
        else:
                raise TypeError("Operand must be a vector or point")
    def __rsub__(self, other):
        if isinstance(other, vector):
            return point(other.x - self.x, other.x - self.y)
        elif isinstance(other, point):
            return vector(other.x - self.x, other.x - self.y)
        else:
                raise TypeError("Operand must be a vector or point")
        
    def __mul__(self, other): 
        if isinstance(other, vector) or isinstance(other, point):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return point(self.x * other, self.y * other)
        else:
            raise TypeError("Operand must be a number, vector or point")
    


class vector:
    def __init__(self, x=0, y=0):
        if isinstance(x, point) and isinstance(y, point):
            self.x = x.x - y.x
            self.y = x.y - y.y
        else:
            self.x = x
            self.y = y
    def __str__(self):
        return f"<{self.x}; {self.y}>"
    
    def __add__(self, other):
        if isinstance(other, vector) or isinstance(other, point):
            return vector(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Operand must be a vector or point")
    __radd__ = __add__

    def __sub__(self, other):
        if isinstance(other, vector) or isinstance(other, point):
            return vector(self.x - other.x, self.y - other.y)
        else:
            raise TypeError("Operand must be a vector or point")
    def __rsub__(self, other):
        if isinstance(other, vector) or isinstance(other, point):
            return point(other.x - self.x, other.y - self.y)
        else:
            raise TypeError("Operand must be a vector or point")
        
    def __mul__(self, other):
        if isinstance(other, vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return vector(self.x * other, self.y * other)
        elif isinstance(other, point):
            raise TypeError("Cannot multiply vector by point")
        else:
            raise TypeError("Operand must be a number or vector")
    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(other, vector):
            return vector(self.x / other.x, self.y / other.y)
        elif isinstance(other, point):
            raise TypeError("Cannot devide vector by point")
        else:
            raise TypeError("Operand must be a vector or point")
    def __rtruediv__(self, other):
        if isinstance(other, vector) or isinstance(other, point):
            return vector(other.x / self.x, other.y / self.y)
        else:
            raise TypeError("Operand must be a vector or point")



vector_1 = vector(point(5, 2), point(1, 4))
print(vector_1)
print(point(1, 2) * vector(3, 4))