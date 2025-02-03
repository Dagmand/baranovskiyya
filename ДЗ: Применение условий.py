def hundred_number_sum():
    hundred_number_sum = 0
    for number in range(1, 101):
        hundred_number_sum += number
    print('Сумма всех чисел диапазона от 1 до 100 равна', hundred_number_sum, end='\n\n')


def user_input_numbers():
    numbers_count = 0
    input_number = float(input('Введите число: '))
    while input_number >= 0:
        try:
            input_number = float(input('Введите число: '))
            numbers_count += 1
        except ValueError:
            print("Ошибка: введено не числовое значение!")
    print ('Кол-во введёных чисел: ', numbers_count, end='\n\n')


hundred_number_sum()

print('Cписок содержащий квадраты всех нечетных чисел от 1 до 10: ', [num ** 2 for num in range(1, 11, 2)], end='\n\n')

user_input_numbers()
