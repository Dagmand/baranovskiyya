def hundred_number_sum():
    hundred_number_sum = 0
    for number in range(1, 101):
        hundred_number_sum += number
    print('Сумма всех чисел диапазона от 1 до 100 равна', hundred_number_sum, end='\n\n')


def user_input_numbers():
    list_input_number = []
    while True:
        try:
            input_number = float(input('Введите число: '))
        except ValueError:
            print("Ошибка: введено не числовое значение!")
        else:
            if input_number >= 0:
                list_input_number.append(input_number)
            else:
                print ('Кол-во введёных чисел: ', len(list_input_number), end='\n\n')
                return False


hundred_number_sum()

print('Cписок содержащий квадраты всех нечетных чисел от 1 до 10: ', [num ** 2 for num in range(1, 11, 2)], end='\n\n')

user_input_numbers()
