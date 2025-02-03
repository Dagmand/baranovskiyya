# from collections import Counter
import string



# list_of_letters = list('абракадабра')

# letter_cnt = Counter(list_of_letters)

# print(letter_cnt)  # Counter({'а': 5, 'б': 2, 'р': 2, 'к': 1, 'д': 1})

# list_of_letters.replace('a')
# # Отсеиваем лишнее
# filtered_dict = {key: value for key, value in letter_cnt.items() if value > 1}
# print(filtered_dict)

# print(list_of_letters)


# def string_to_list(input_string: str) -> list:
#     punctuation = '!"#$%&\'()*+,—-./:;<=>?@[\\]^_`{|}~'
#     for simbol in punctuation:
#         if  simbol in input_string:
#             input_string = input_string.replace(simbol, '')
#     return input_string.split()


def string_to_list(input_string: str) -> list:
    for simbol in input_string:
        if  simbol in string.punctuation:
            input_string = input_string.replace(simbol, '')
    return input_string.split()



user_text = str(input('Введите Ваш текст: ').lower())

print(string_to_list(user_text))
