try:
    user_age = int(input('Введите Ваш возраст (полных лет): '))
    user_nationality = str(input('Являетесь ли Вы гражданином (Да или Нет): '))
    user_criminal_record = str(input('Имеется ли у Вас судимость (Да или Нет): '))
except ValueError:
    print('Ошибка: Введены не корректные данные')
else:
    if user_age >= 18 and user_nationality == 'Да' and user_criminal_record == 'Нет':
        print('Вы допущены до голосования')
    elif user_age < 18 or user_nationality == 'Нет' or user_criminal_record == 'Да':
        print('Вы не допущены до голосования')
    else:
        print('Ошибка: Введены не корректные данные')
