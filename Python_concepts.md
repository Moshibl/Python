# Python Concepts Summary

## DataClass

A `dataclass` in Python is a special decorator introduced in Python 3.7 that simplifies class creation for data storage. It automatically generates methods like `__init__`, `__repr__`, and `__eq__`, reducing boilerplate code.

```python
from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    year: int

book = Book('1984', 'George Orwell', 1949)
print(book)  # Output: Book(title='1984', author='George Orwell', year=1949)
```

---

## Multiple Inheritance

Multiple inheritance in Python follows the **Method Resolution Order (MRO)**, which determines the sequence in which parent classes are searched for methods and attributes. The **C3 linearization algorithm** ensures consistency.

```python
class X:
    def show(self):
        print('Class X')

class Y(X):
    def show(self):
        print('Class Y')

class Z(X):
    def show(self):
        print('Class Z')

class M(Y, Z):
    pass

m = M()
m.show()  # Output: Class Y
print(M.__mro__)  # Output: (<class '__main__.M'>, <class '__main__.Y'>, <class '__main__.Z'>, <class '__main__.X'>, <class 'object'>)
```

---

## Dictionary Comprehension

A concise way to create dictionaries using a single line of code.

```python
cubes = {x: x**3 for x in range(1, 6)}
print(cubes)  # Output: {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
```

---

## Composition

Composition allows objects to contain other objects as attributes, promoting code reuse and modularity.

```python
class Battery:
    def __init__(self, capacity):
        self.capacity = capacity

    def __str__(self):
        return f'{self.capacity}mAh battery'

class Phone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.battery = battery

    def phone_info(self):
        return f'{self.brand} {self.model} with a {self.battery}'

battery1 = Battery(5000)
phone1 = Phone('Samsung', 'Galaxy S22', battery1)

print(phone1.phone_info())  # Output: Samsung Galaxy S22 with a 5000mAh battery
```

---

## Vector Class

A class implementing vector operations such as addition, subtraction, multiplication, and indexing.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def magnitude(self):
        return (self.x**2 + self.y**2)**0.5

    def __getitem__(self, index):
        return (self.x, self.y)[index]

# Example usage:
v1 = Vector(5, 7)
v2 = Vector(2, 3)

print(v1)                   # Output: Vector(5, 7)
print(v1 + v2)              # Output: Vector(7, 10)
print(v1 - v2)              # Output: Vector(3, 4)
print(v1 * 2)               # Output: Vector(10, 14)
print(v1 == Vector(5, 7))   # Output: True
print(v1.magnitude())       # Output: 8.6 (approx)
print(v1[0])                # Output: 5 (x component)
print(v1[1])                # Output: 7 (y component)
```

