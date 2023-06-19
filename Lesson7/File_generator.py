from random import randint
from os import mkdir, chdir
from os.path import isdir, isfile


from Names_generator import get_name


def change_work_folder(folder_name: str):
    if not isdir(folder_name):
        mkdir(folder_name)
    chdir(folder_name)


def mult_file_gen(extensions_numbers: list[tuple[str, int]], is_in_folder: bool = False,
                  name_folder: str = 'new_folder'):
    if is_in_folder:
        change_work_folder(name_folder)
    for item in extensions_numbers:
        ext, numbers = item
        file_gen(ext, file_numbers=numbers)


def file_gen(extension: str, min_len_name: int = 6, max_len_name=30, min_bytes_number: int = 256,
             max_bytes_number: int = 4096, file_numbers: int = 42):
    for _ in range(file_numbers):
        file_name = f'{get_name(min_len_name, max_len_name)}.{extension}'
        if not isfile(file_name):
            with open(f'{get_name(min_len_name, max_len_name)}.{extension}', 'bw') as f:
                f.write(bytes(randint(0, 255) for _ in range(randint(min_bytes_number, max_bytes_number))))


if __name__ == '__main__':
    mult_file_gen([('bin', 1), ('txt', 2)], True)
