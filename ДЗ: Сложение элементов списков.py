evens = [1, 3, 5, 7, 9]
odds = [0, 2, 4, 6, 8, 10]

sum_of_numbers = []

for i in range(max(len(evens), len(odds))):
    try:
        sum_of_numbers.append(evens[i] + odds[i])
    except IndexError:
        if len(evens) < len(odds):
            sum_of_numbers.append(odds[i])
        else:
            sum_of_numbers.append(evens[i])

print(sum)

