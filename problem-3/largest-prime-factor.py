def largest_factor(num):
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
    return num

print(largest_factor(600851475143))
