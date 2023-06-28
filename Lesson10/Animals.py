class Animal:
    def __init__(self, name=None, age=None, food_type='all'):
        self.name = name
        self.age = age
        self.food_type = food_type


class Fish(Animal):
    def __init__(self, fins_number=0, *args, **kwargs):
        self._fins_number = fins_number
        super().__init__(*args, **kwargs)

    def fins_number(self):
        return self.fins_number


class Beast(Animal):
    def __init__(self, is_wool=False, hair_color=None, *args, **kwargs):
        self._is_wool = is_wool
        self._hair_color = hair_color
        super().__init__(*args, **kwargs)

    def have_wool(self):
        return self._is_wool

    def hair_color(self):
        return self._hair_color


class Reptile(Animal):
    def __init__(self, leg_number=0, *args, **kwargs):
        self._leg_number = leg_number
        super().__init__(*args, **kwargs)

    def leg_number(self):
        return self._leg_number


class Animal_Factory:
    def __init__(self, animal_type='Beast', *args, **kwargs):
        self.animal_class = None
        if animal_type == 'Beast':
            self.animal_class = Beast(*args, **kwargs)
        elif animal_type == 'Reptile':
            self.animal_class = Reptile(*args, **kwargs)
        elif animal_type == 'Fish':
            self.animal_class = Fish(*args, **kwargs)
        else:
            self.animal_class = Animal(*args, **kwargs)

    def get_animal(self) -> Animal:
        return self.animal_class


if __name__ == '__main__':
    factory = Animal_Factory('Reptile', name='Something', age=16, leg_number=4)
    print(factory.get_animal())