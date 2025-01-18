def max_number(a, b):
    if a >= b:
        return a
    else:
        return b


def empty_function():
    pass


def even_numbers(n):
    for i in range(0, n+1):
        if i!= 0 and i % 2 == 0:
            yield i


def test_max_number():
    assert max_number(1, 2) == 2
    assert max_number(3, -2) == 3
    assert max_number(1, 1) == 1


even_generator = even_numbers(9)
for i in even_generator:
    print(i)

