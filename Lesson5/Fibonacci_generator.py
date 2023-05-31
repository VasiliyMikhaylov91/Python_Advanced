def fibonacci_gen(number: int):
    first = 1
    second = 1
    yield first
    for _ in range(1, number):
        yield second
        temp = second
        second += first
        first = temp


if __name__ == '__main__':
    print(*fibonacci_gen(20))