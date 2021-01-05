# super() - call methods of the superclass in your subclass
#
# By using inheritance, you can reduce the amount of code you write while
# simultaneously reflecting the real-world relationship between rectangles and
# squares:
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


# Because Cube inherits from Square and .__init__() doesn’t really do anything
# differently for Cube than it already does for Square, you can skip defining
# it, and the .__init__() of the superclass (Square) will be called
# automatically:
class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def tri_area(self):
        return 0.5 * self.base * self.height


class RightPyramid(Triangle, Square):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area

    def area_2(self):
        base_area = super().area()
        triangle_area = super().tri_area()
        return triangle_area * 4 + base_area


# ------------------------------------------------------------------------------

# Class example:
class Employee:
    raise_amt = 1.04

    def __repr__(self):
        return f"{self.first} {self.last}"

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.email = f"{first}_{last}@email.com"
        self.salary = salary

    def __add__(self, other):
        return self.salary + other.salary

    def fullname(self):
        return f"{self.first} {self.last}"

    def test(self):
        return True


class Developer(Employee):
    raise_amt = 1.10

    def __repr__(self):
        return super().__repr__()

    def __init__(self, first, last, salary, prog_lang):
        super().__init__(first, last, salary)
        self.prog_lang = prog_lang

    def test2(self):
        pass


class Manager(Employee):
    def __init__(self, first, last, salary, employees=None):
        super().__init__(first, last, salary)
        if employees is None:
            self.emlpoyees = []
        else:
            self.emlpoyees = employees

    def add_emp(self, emp):
        if emp not in self.emlpoyees:
            self.emlpoyees.append(emp)

    def remove_emp(self, emp):
        if emp not in self.emlpoyees:
            self.emlpoyees.remove(emp)

    def print_emp(self):
        for emp in self.emlpoyees:
            print(f"--> {emp.fullname()}")


dev_1 = Developer("Jacek", "Balcerzak", 4000, "java")
dev_2 = Developer("Marek", "Marecki", 6000, "python")

mgr_1 = Manager("Jarek", "Wazniak", 10000, [dev_1])

print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.print_emp()
