def squares_sum():
    number = 100
    result = 0
    for _ in range(number + 1):
        result += sum([i_num**2 for i_num in range(10000)])

    return result

# print(squares_sum())

my_func = squares_sum
print(my_func)

my_func = squares_sum()
print(my_func)