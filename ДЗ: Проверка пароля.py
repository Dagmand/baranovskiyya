user_password = 'Zz1123!'

validate_password = ''

while validate_password != user_password:
    validate_password = str(input('Введите пароль: '))
    if validate_password == user_password:
        print('Вы ввели верный пароль.')
    else:
        print('Вы ввели неверный пароль! Попробуйте ещё раз.')
else:
    print('Цикл завершён.')
