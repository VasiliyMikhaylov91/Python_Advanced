LOW_NUMBER = 2
MAX_NUMBER = 10

for i in range(LOW_NUMBER, MAX_NUMBER):
    for j in range (LOW_NUMBER, MAX_NUMBER + 1):
        print(f'{i} X {j} = {i * j}')
    print()