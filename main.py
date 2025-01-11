#Калькулятор

result_operation = ''
result = 0

try:
    
    number_1 = int(input('Введите первое число: '))
    number_2 = int(input('Введите второе число: '))
    operation = input('Введите оператор: ')

    if operation == '+':
        result = number_1 + number_2
        result_operation = 'Результат сложения:'
    elif operation == '-':
        result = number_1 - number_2
        result_operation = 'Результат разности:'
    elif operation == '*':
        result = number_1 * number_2
        result_operation = 'Результат умножения:'
    elif operation == '/':
        result = number_1 / number_2
        result_operation = 'Результат деления:'
    else:
        print('Введён не верный оператор')

except ValueError:
    print('Ошибка: введено не числовое значение!')
except ZeroDivisionError:
    print('Ошибка: Деление на ноль!')

else:
    print(result_operation, result)
