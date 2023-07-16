import logging
import argparse

logging.basicConfig(filename='log.log', encoding='utf-8', level=logging.NOTSET)
logger = logging.getLogger('main')


class Rectangle_Exception(ValueError):
    def __init__(self, value):
        self.value = value
        logger.critical(f'Попытка создания прямоугольника со стороной {self.value}')

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
        logger.info(f'Создан прямоугольник со сторонами {self.a} и {self.b}')

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
        logger.debug('Сложение прямоугольников {self} и {other} успешно')
        return Rectangle(a, b)

    def __sub__(self, other):
        '''Calculation sub two rectangles'''
        new_perimetr = abs(self.perimetr() - other.perimetr())
        a = min(self.a, self.b, other.a, other.b)
        b = new_perimetr // 2
        logger.debug(f'Вычитание прямоугольников {self} и {other} успешно')
        return Rectangle(a, b)

    def __eq__(self, other):
        '''If two given rectangles have same area return True else return False'''
        logger.info(f'Сравнение прямоугольников {self} == {other}')
        return self.area() == other.area()

    def __ne__(self, other):
        '''If two given rectangles have not same area return True else return False'''
        logger.info(f'Сравнение прямоугольников {self} != {other}')
        return self.area() != other.area()

    def __ge__(self, other):
        '''If self rectangle area >= other rectangle area return True else False'''
        logger.info(f'Сравнение прямоугольников {self} >= {other}')
        return self.area() >= other.area()

    def __gt__(self, other):
        '''If self rectangle area > other rectangle area return True else False'''
        logger.info(f'Сравнение прямоугольников {self} > {other}')
        return self.area() > other.area()

    def __le__(self, other):
        '''If self rectangle area <= other rectangle area return True else False'''
        logger.info(f'Сравнение прямоугольников {self} <= {other}')
        return self.area() <= other.area()

    def __lt__(self, other):
        '''If self rectangle area < other rectangle area return True else False'''
        logger.info(f'Сравнение прямоугольников {self} < {other}')
        return self.area() < other.area()

    def __repr__(self):
        return f'Rectangle({self.a}, {self.b})'


def args_operation(ars: list[str]) -> bool or Rectangle:
    rect1_list = []
    rect2_list = []
    operation = None
    inp_rect1 = True

    for item in ars:
        if inp_rect1:
            if item.isdigit():
                rect1_list.append(int(item))
            else:
                operation = item
                inp_rect1 = False
        else:
            rect2_list.append(int(item))

    try:
        match operation:
            case '+':
                return Rectangle(*rect1_list) + Rectangle(*rect2_list)
            case '-':
                return Rectangle(*rect1_list) - Rectangle(*rect2_list)
            case '==':
                return Rectangle(*rect1_list) == Rectangle(*rect2_list)
            case '!=':
                return Rectangle(*rect1_list) != Rectangle(*rect2_list)
            case '>=':
                return Rectangle(*rect1_list) >= Rectangle(*rect2_list)
            case '>':
                return Rectangle(*rect1_list) > Rectangle(*rect2_list)
            case '<=':
                return Rectangle(*rect1_list) <= Rectangle(*rect2_list)
            case '<':
                return Rectangle(*rect1_list) < Rectangle(*rect2_list)
            case _:
                raise AttributeError('Неверный ввод')
    except AttributeError as e:
        logger.critical(msg=e)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Rectanrgle operation parser')
    parser.add_argument('input', metavar='INP', type=str, nargs='*',
                        help='Input 2 rectangles parameters and operation between')
    args = parser.parse_args().input
    print(args_operation(args))
