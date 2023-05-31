def spliter(abs_address: str) -> tuple:
    adr_index = abs_address.rfind('/')
    point_index = abs_address.rfind('.')
    return abs_address[:adr_index + 1], abs_address[adr_index + 1:point_index], abs_address[point_index + 1:]


if __name__ == '__main__':
    print(spliter('D:/GeekBrains/Python_Advanced/Lesson5/Path_name_ext_spliter.py'))
