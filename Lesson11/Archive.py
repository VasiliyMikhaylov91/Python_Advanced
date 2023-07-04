class Archive:
    '''Save number and string for each example. All examples saves to list'''
    archives = []

    def __new__(cls, number: int, value: str):
        '''Create parameters number and value for example, and append it to list'''
        instance = super().__new__(cls)
        instance.number = number
        instance.value = value
        cls.archives.append(instance)
        return instance

    def __repr__(self):
        '''Return representation for developer'''
        return f'Archive({self.number}, {self.value})'

    def __str__(self):
        '''Return representation for user'''
        return f'N = {self.number}  Value = {self.value}'


if __name__ == '__main__':
    a1 = Archive(12, 'afgesgvs')
    a2 = Archive(1, 'asgszx')
    print([(x.number, x.value) for x in Archive.archives])
    print(a1.__repr__())
    print(a1)
    help(Archive)