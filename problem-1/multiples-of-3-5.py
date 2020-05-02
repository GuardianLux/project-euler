def multiples_of_3_5():
    sum_multiples = 0
    i = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            sum_multiples += i
        i += 1
    return sum_multiples


print(multiples_of_3_5())