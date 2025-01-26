user_text = str(input('Введите Ваш текст: ').lower())

user_text_list = []
user_text_without_punctuation = ''
vowels_count = 0
longest_word = ''
similar_word_count = 0
multi_word_check = []

for letter in user_text:
    if  letter in '!"#$%&\'()*+,—-./:;<=>?@[\\]^_`{|}~':
        continue
    elif letter in 'аеёиоуыэюя':
            vowels_count += 1
            user_text_without_punctuation += letter
    else:
        user_text_without_punctuation += letter


user_text_list = user_text_without_punctuation.split()


for word in user_text_list:
    if len(word) > len(longest_word):
        longest_word = word
    elif len(word) == len(longest_word):
        continue


print('Кол-во слов с тексте: ', len(user_text_list))
print('Самое длинное слово: ', longest_word)
print('Количество гласных букв: ', vowels_count)


for word_a in user_text_list:
    if word_a in multi_word_check:
        continue
    else:
        for word_b in user_text_list:
            if word_a == word_b:
                similar_word_count += 1
    multi_word_check.append(word_a)
    print(f'Слово \'{word_a}\' встречается в строке {similar_word_count} раз')
    similar_word_count = 0
