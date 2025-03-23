evens = [1, 3, 5, 7, 9, 10]
odds = [0, 2, 4, 6, 8]

sum = []

for i in range(max(len(evens), len(odds))):
    try:
        sum.append(evens[i] + odds[i])
    except IndexError:
        if i >= min(len(evens), len(odds)):
            if len(evens) == i + 1 and len(evens) < len(odds):
                sum.append(odds[i])
            else:
                sum.append(evens[i])

print(sum)

