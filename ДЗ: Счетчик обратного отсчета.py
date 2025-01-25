reverse_counter = int(input('Введите число начала отсчёта: ').strip()) + 1

while reverse_counter != 0:
    reverse_counter -= 1
    print(reverse_counter)
else:
    print('Отсчёт окончен')
