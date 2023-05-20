def my_hex(dec_number: int) -> str:
    notation = 16
    hex_dict = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    result = ''

    while dec_number:
        remainder = dec_number % notation
        latter = hex_dict[remainder] if remainder in hex_dict else str(remainder)
        result = latter + result
        dec_number //= notation
    return result


if __name__ == '__main__':
    print(my_hex(192), hex(192))
