RATE = 50.0
TAX_PERCENT = 1.5
MIN_TAX = 30.0
MAX_TAX = 600.0
BONUS_PERCENT = 3.0
BONUS_COUNT = 3
RICH_SUM_OVER = 5_000_000.0
RICH_TAX_PERCENT = 10.0
MAX_PERCENT = 100.0

balance = 0.0
operation_count = 0
operation_list = []

def rich_tax():
    global balance
    if balance > RICH_SUM_OVER:
        balance *= (1 - RICH_TAX_PERCENT / MAX_PERCENT)


def rise_balance(cache: int) -> str:
    global balance, operation_count, operation_list
    result = ''

    if not cache % RATE:
        balance += cache
        operation_count += 1
        if not operation_count % BONUS_COUNT:
            balance += balance * BONUS_PERCENT / MAX_PERCENT
        result += 'Операция зачисления выполнена успешно. '
        operation_list.append(f'Операция зачисления {cache}')
    else:
        result += 'Введите сумму кратную 50. '

    rich_tax()
    result += f'Баланс: {balance}'
    return result


def reduce_balance(cache: int) -> str:
    global balance, operation_count
    result = ''
    tax = cache * TAX_PERCENT / MAX_PERCENT
    if tax < MIN_TAX:
        tax = MIN_TAX
    if tax > MAX_TAX:
        tax = MAX_TAX

    if not cache % RATE and cache <= balance:
        balance -= cache + tax
        operation_count += 1
        if not operation_count % BONUS_COUNT:
            balance += balance * (BONUS_PERCENT / MAX_PERCENT)
        result += 'Операция снятия выполнена успешно. '
        operation_list.append(f'Операция снятия {cache}')
    else:
        result += 'Выведите сумму кратную 50. '

    rich_tax()
    result += f'Баланс: {balance}'
    return result


def exiting() -> str:  # Не указано, что должна делать операция
    # rich_tax()
    return 'Всего хорошего!'


if __name__ == '__main__':
    print(rise_balance(5_000_000))
    print(rise_balance(50))
    print(rise_balance(70))
    print(reduce_balance(45))
    print(reduce_balance(50))
    print(operation_list)
    print(exiting())