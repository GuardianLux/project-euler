i = 1
prime = 0
counter = 0

for i in range(2, prime):
    if (i % prime) == 0:
        counter += 1
    if counter == 10001:
        prime = i
print(prime)
