class Rectangle_Exception(ValueError):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Задана сторона с длинной {self.value}\n' \
               f'Невозможно сознать прямоугольник с отрицательным значением стороны'

class Rectangle:
    '''Creating rectangle by two sides'''

    def __init__(self, a: int, b: int = None):
        '''Initialisation new rectangle by a and b sides'''
        if a < 0:
            raise Rectangle_Exception(a)
        if b < 0:
            raise Rectangle_Exception(b)
        self.a = a
        self.b = b if b is not None else a

    def perimetr(self):
        '''Calculation rectangle perimetr'''
        return 2 * (self.a + self.b)

    def area(self):
        '''Calculation rectangle area'''
        return self.a * self.b

    def __add__(self, other):
        '''Calculation sum two rectangles'''
        new_perimetr = self.perimetr() + other.perimetr()
        a = self.a
        b = new_perimetr // 2 - a
        return Rectangle(a, b)

    def __sub__(self, other):
        '''Calculation sub two rectangles'''
        new_perimetr = abs(self.perimetr() - other.perimetr())
        a = min(self.a, self.b, other.a, other.b)
        b = new_perimetr // 2
        return Rectangle(a, b)

    def __eq__(self, other):
        '''If two given rectangles have same area return True else return False'''
        return self.area() == other.area()

    def __ne__(self, other):
        '''If two given rectangles have not same area return True else return False'''
        return self.area() != other.area()

    def __ge__(self, other):
        '''If self rectangle area >= other rectangle area return True else False'''
        return self.area() >= other.area()

    def __gt__(self, other):
        '''If self rectangle area > other rectangle area return True else False'''
        return self.area() > other.area()

    def __le__(self, other):
        '''If self rectangle area <= other rectangle area return True else False'''
        return self.area() <= other.area()

    def __lt__(self, other):
        '''If self rectangle area < other rectangle area return True else False'''
        return self.area() < other.area()


if __name__ == '__main__':
    rect1 = Rectangle(-5)
    rect2 = Rectangle(5, 10)
    rect_add = rect1 + rect2
    rect_sub = rect1 - rect2
    print(f'{rect_add.a = } {rect_add.b = }')
    print(f'{rect_sub.a = } {rect_sub.b = }')