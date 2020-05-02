def even_fibonacci_sum():
    a, b = 1, 2
    while a < 4000000:
        if a % 2 == 0:
            yield a
        a, b = b, a + b


print(sum(even_fibonacci_sum()))