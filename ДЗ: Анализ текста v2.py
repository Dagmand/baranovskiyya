# Подсчитывает количество слов в тексте.

# Определяет самое длинное слово в тексте.

# Подсчитывает количество гласных букв (а, е, ё, и, о, у, ы, э, ю, я) в тексте.

# Выводит количество раз, которое каждое слово встречается в тексте.

from collections import Counter

# Работает
def string_to_list(input_string: str) -> list:
    user_text_without_punctuation = ''
    for letter in input_string:
        if  letter in '!"#$%&\'()*+,—-./:;<=>?@[\\]^_`{|}~':
            continue
        else:
            user_text_without_punctuation += letter
    return user_text_without_punctuation.split()


# Работает
def len_list(list: list):
    return(len(list))


def longest_word(list: list) -> str:
    longest_word = ''
    for word in list:
        if len(word) > len(longest_word):
            longest_word = word
        else:
            continue
    return longest_word


# Работает
def vowels_count(text: str) -> int:
    to_list = list(user_text)
    sample_vowels = 'аеёиоуыэюя'
    vowels = [1 for letter in to_list if letter in sample_vowels]
    vowels_count = sum(vowels)
    return vowels_count


# Работает
def same_words_count(list: list) -> dict:
    same_words_count = Counter(string_to_list(user_text))
    return same_words_count


user_text = str(input('Введите Ваш текст: ').lower())

# print(string_to_list(user_text))
print('Кол-во слов в тексте: ', len_list(string_to_list(user_text)), end='\n\n')
print('Самое длинное слово в тексте:', longest_word(string_to_list(user_text)), end='\n\n')
print('Кол-во гласных в тексте: ', vowels_count(user_text), end='\n\n')

for key, value in same_words_count(string_to_list(user_text)).items():
    print(f'Кол-во повторений слова \"{key}\" в тексте: {value}', sep='\n')
# print(same_words_count(string_to_list(user_text)))