import numpy as np

arr = np.arange(1, 101)
sum_of_squares = np.sum(np.square(arr))
square_of_sum = np.sum(arr) ** 2
difference = sum_of_squares - square_of_sum
print(abs(difference))