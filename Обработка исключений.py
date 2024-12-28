#Обработка исключений

try:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    result = num1 / num2
except ValueError:
    print("Ошибка: введено не числовое значение!")
except ZeroDivisionError:
    print("Ошибка: Деление на ноль!")
else:
    print(result)
finally:
    print("Работа программы завершена")