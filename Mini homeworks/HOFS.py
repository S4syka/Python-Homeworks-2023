from functools import reduce, partial
import operator
import itertools

# List of numbers
numbers = [1, 2, 3, 4, 5]

# 1. map - applies a function to all items in the input list
squared_numbers = map(lambda x: x ** 2, numbers)
print(f"1. Squared Numbers using map: {list(squared_numbers)}")

# 2. filter - creates a list of elements for which a function returns true
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(f"2. Even Numbers using filter: {list(even_numbers)}")

# 3. reduce - applies a rolling computation to sequential pairs of values in a list
product = reduce(lambda x, y: x * y, numbers)
print(f"3. Product of all numbers using reduce: {product}")

# 4. sorted - sorts the elements
sorted_numbers = sorted(numbers, key=lambda x: -x)
print(f"4. Numbers in descending order using sorted: {sorted_numbers}")

# 5. any - returns True if at least one element of an iterable is true
is_any_even = any(x % 2 == 0 for x in numbers)
print(f"5. Is any number even using any: {is_any_even}")

# 6. all - returns True if all elements of an iterable are true
are_all_positive = all(x > 0 for x in numbers)
print(f"6. Are all numbers positive using all: {are_all_positive}")

# 7. enumerate - returns an enumerate object
enumerated_numbers = enumerate(numbers, start=1)
print(f"7. Enumerated numbers using enumerate: {list(enumerated_numbers)}")

# 8. zip - aggregates elements from two or more iterables
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
zipped = zip(names, ages)
print(f"8. Zipped lists using zip: {list(zipped)}")

# 9. partial - returns a new partial object which behaves like func called with the partial arguments
def power(base, exponent):
    return base ** exponent
square = partial(power, exponent=2)
print(f"9. Square of 4 using partial: {square(4)}")

# 10. accumulate - returns accumulated results
accumulated = itertools.accumulate(numbers, operator.mul)
print(f"10. Accumulated product using accumulate: {list(accumulated)}")
