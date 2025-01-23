try:
    user_age = int(input('Введите Ваш возраст (полных лет): '))
    user_nationality = str(input('Являетесь ли Вы гражданином (Да или Нет): '))
    user_criminal_record = str(input('Имеется ли у Вас судимость (Да или Нет): '))
except ValueError:
    print('Ошибка: Введены не корректные данные')
else:
    if  18 <= user_age <= 100 and user_nationality.lower().strip() == 'да' and user_criminal_record.lower().strip() == 'Нет':
        print('Вы допущены до голосования')
    elif user_age < 18 or user_nationality.lower().strip() == 'нет' or user_criminal_record.lower().strip() == 'да':
        print('Вы не допущены до голосования')
    else:
        print('Ошибка: Введены не корректные данные')
