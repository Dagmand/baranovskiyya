#Калькулятор

result = 0

try:
    
    number_1 = int(input('Введите первое число: '))
    number_2 = int(input('Введите первое число: '))

except ValueError:
    print("Ошибка: введено не числовое значение!")

else:
    operation = input('Введите оператор: ')

    if operation == '+':
        result = number_1 + number_2
        print('Результат сложения:', result)
    elif operation == '-':
        result = number_1 - number_2
        print('Результат разности:', result)
    elif operation == '*':
        result = number_1 * number_2
        print('Результат умножения:', result)
    elif operation == '/':
        try:
            result = number_1 / number_2
        except ZeroDivisionError:
            print("Ошибка: Деление на ноль!")
        else:
            print('Результат деления:', result)
    else:
        print('Введён не верный оператор')
