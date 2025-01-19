def max_number(a, b):
    if a >= b:
        return a
    else:
        return b


def empty_function():
    pass


def even_numbers(n):
    for i in range(0, n+1):
        if i!= 0 and i % 2 == 0:
            yield i


def test_max_number():
    assert max_number(1, 2) == 2, "Ошибка: результат не является наибольшей цифрой"
    assert max_number(3, -5) == 3, "Ошибка: не учитывается знак '-'"


max_number_result = max_number(3, 6)
print(f'Результат выполнения функции "max_number": {max_number_result}', end='\n\n')

test_empty_function = empty_function()
print(f'Результат выполнения функции "test_empty_function": {test_empty_function}', end='\n\n')

even_generator = even_numbers(9)
print('Результат выполнения функции "even_numbers"','\nЧетные цифры от 0 до 9:')
for i in even_generator:
    print(i)

test_max_number()
print('\nРезультат выполнения функции "test_max_number":', '\nВсе тесты пройдены!')
