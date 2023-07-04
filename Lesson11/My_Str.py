from time import time


class My_Str(str):
    '''Extend class str. Added author and creation time str'''

    def __new__(cls, value: str, author: str):
        '''New parameters for class'''
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time_create = time()
        return instance


if __name__ == '__main__':
    s = My_Str('asdf', 'vasiliy')
    print(s.author)
    print(s.time_create)
    print(s)
    help(My_Str)
