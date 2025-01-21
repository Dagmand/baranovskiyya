user_age = int(input('Введите Ваш возраст (полных лет): '))
user_nationality = str(input('Являетесь ли Вы гражданином (Да или Нет): '))
user_criminal_record = str(input('Имеется ли у Вас судимость (Да или Нет): '))

age_status = 'достаточно' if user_age >= 18 else 'не достаточно'
nationality_status = 'гражданин' if user_nationality == 'Да' else 'не гражданин'
criminal_status = 'есть судимость' if user_criminal_record == 'Да' else 'нет судимости'

decision = True if user_age >= 18 and user_nationality == 'Да' else False

print(f'Вам {age_status} лет. Вы {nationality_status} страны. У Вас {criminal_status}.')
print('Вы допущены до голосования' if decision == True else 'Вы не допущены до голосования')
