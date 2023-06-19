from random import randint, choice

VOWELS = 'aeioy'
CONSONANT = 'bcdfghjklmnopqrstvwxz'


def get_name(min_length: int = 4, max_length: int = 7) -> str:
    name = choice(VOWELS + CONSONANT)
    for i in range(randint(min_length - 1, max_length - 1)):
        name += choice(VOWELS if not i % 3 else CONSONANT)
    return name.capitalize()


def save_names(names_numbers: int, file_name: str):
    with open(file_name, 'w', encoding='utf-8') as f:
        for _ in range(names_numbers):
            f.write(f'{get_name()}\n')


if __name__ == '__main__':
    save_names(6, 'names.txt')
