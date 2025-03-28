import string 


def string_to_list(input_string: str) -> list:
    for simbol in input_string:
        if  simbol in string.punctuation:
            input_string = input_string.replace(simbol, '')
    return input_string.split()


def longest_word(list: list) -> str:
    longest_word = ''
    for word in list:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word


def vowels_count(text: str) -> int:
    to_list = list(text)
    sample_vowels = 'аеёиоуыэюя'
    vowels = [1 for letter in to_list if letter in sample_vowels]
    vowels_count = sum(vowels)
    return vowels_count


def same_words_count(list: list) -> dict:
    same_words_count = {}
    for word in list:
        same_words_count[word] = same_words_count.get(word, 0) + 1
    return same_words_count


user_text = str(input('Введите Ваш текст: ').lower())

print('Кол-во слов в тексте: ', len(string_to_list(user_text)), end='\n\n')
print('Самое длинное слово в тексте:', longest_word(string_to_list(user_text)), end='\n\n')
print('Кол-во гласных в тексте: ', vowels_count(user_text), end='\n\n')

for key, value in same_words_count(string_to_list(user_text)).items():
    print(f'Кол-во повторений слова \"{key}\" в тексте: {value}', sep='\n')
