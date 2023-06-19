from os import listdir, rename
from os.path import isfile


def _int_count_to_str(count_value: int, digits_number: int) -> str:
    start_str = str(count_value)
    zeros_number = digits_number - len(start_str)
    if zeros_number < 0:
        zeros_number = 0
    return '0' * zeros_number + start_str


def rename_files(digits_in_number: int, rename_extension: str, result_extension: str,
                 range_source_name: list[int, int], res_name: str = ''):
    count_files = 1
    for obj in listdir():
        if isfile(obj) and obj.endswith(rename_extension):
            old_name = obj
            rename(obj, old_name[range_source_name[0]: range_source_name[1] + 1] +
                   '_' +
                   res_name +
                   _int_count_to_str(count_files, digits_in_number) +
                   '.' +
                   result_extension)
            count_files += 1

