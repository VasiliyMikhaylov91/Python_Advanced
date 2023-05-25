'''
Пользователь вводит данные. Сделайте проверку данных и преобразуйте если возможно в один из вариантов ниже:
целое положительное число
вещественное положительное или отрицательное число
строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
строку в верхнем регистре в остальных случаях
'''

def task2():
    input_data = input("Enter data: ")
    if input_data.isdigit():
        result = int(input_data)
    elif (input_data.count(".") == 1 or (input_data.count("-") == 1
                                         and input_data.startswith("-"))) \
            and (input_data.replace("-", "").replace(".", "").isdigit()):
        result = float(input_data)
    elif not input_data.islower():
        result = input_data.lower()
    else:
        result = input_data.upper()
    print(f"{result}")


task2()