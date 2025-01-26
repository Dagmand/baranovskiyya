# Подсчитывает количество слов в тексте.

# Определяет самое длинное слово в тексте.

# Подсчитывает количество гласных букв (а, е, ё, и, о, у, ы, э, ю, я) в тексте.

# Выводит количество раз, которое каждое слово встречается в тексте.


def string_to_list(input_string: str) -> list:
    user_text_without_punctuation = ''
    for letter in input_string:
        if  letter in '!"#$%&\'()*+,—-./:;<=>?@[\\]^_`{|}~':
            continue
        else:
            user_text_without_punctuation += letter
    return user_text_without_punctuation.split()


def len_list(list: list):
    return(len(list))


def vowels_count(text: str) -> int:
    vowels_count = 0
    for letter in text:
        if letter in 'аеёиоуыэюя':
            vowels_count += 1
    return vowels_count


def words_count(list: list):
    multi_word_check = []
    similar_word_count = 0
    for word_a in string_to_list(user_text):
        if word_a in multi_word_check:
            continue
        else:
            for word_b in string_to_list(user_text):
                if word_a == word_b:
                    similar_word_count += 1
    multi_word_check.append(word_a)
    print(f'Слово \'{word_a}\' встречается в строке {similar_word_count} раз')
    similar_word_count = 0


user_text = str(input('Введите Ваш текст: ').lower())

# print(string_to_list(user_text))
print('Кол-во слов в тексте: ', len_list(string_to_list(user_text)), end='\n\n')
print('Кол-во гласных в тексте: ', vowels_count(user_text), end='\n\n')
print('Кол-во повторений слов в тексте: ', words_count(user_text), end='\n\n')
