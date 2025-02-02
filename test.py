from collections import Counter

list_of_letters = list('абракадабра')

letter_cnt = Counter(list_of_letters)

print(letter_cnt)  # Counter({'а': 5, 'б': 2, 'р': 2, 'к': 1, 'д': 1})


# Отсеиваем лишнее
filtered_dict = {key: value for key, value in letter_cnt.items() if value > 1}
print(filtered_dict)