class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        result = self.quantity - other.quantity
        if result > 0:
            return Cell(result)
        else:
            return f'Вычитание не возможно, так как результат меньше 0'

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        return Cell(self.quantity // other.quantity)

    def __str__(self):
        return str(self.quantity)

    def make_order(self, row_length):
        return ('*' * row_length + '\n') * (self.quantity // row_length) + '*' * (self.quantity % row_length)


a = Cell(10)
b = Cell(11)
c = Cell(32)
d = Cell(25)
e = Cell(2)
f = Cell(1)

print(a + b)
print(b - c)
print(c - b)
print(d * e)
print(e / f)
print(d.make_order(10))