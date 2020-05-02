def multiples_of_3_5():
    sum = 0
    i = 0
    for i in range(1000):
        if i%3 == 0 or i%5 == 0:
            sum += i
        i += 1
    print("The sum of all multiples of 3 & 5 below 1000 are: " + str(sum))