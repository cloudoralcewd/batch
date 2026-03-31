# TUPLE BASICS

# List - []
# tuple - ()
# set - {}

# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Defining a tuple with geographical coordinates
location = (40.7128, -74.0060)  # Latitude and Longitude of New York City
print(f'Type of location: {type(location)}')
print(f'Location: {location}')
print(f'Latitude: {location[0]}')
print(f'Longitude: {location[1]}')

# location[0] = 34.0522

empty_tuple_1 = ()
empty_tuple_2 = tuple()
print(f'Empty Tuple 1: {empty_tuple_1}')
print(f'Empty Tuple 2: {empty_tuple_2}')

# A single-element tuple requires a trailing comma
number = 10,
print(f'Number: {number}, Type: {type(number)}')

nums = (1, 2, 3, 4, 5)
tmp_nums = list(nums)
tmp_nums.append(6)
nums = tuple(tmp_nums)
print(f'Number: {nums}, Type: {type(nums)}')

# TUPLE UNPACKING
# location = (40.7128, -74.0060)
latitude, longitude = location
a, b = location

print(f'Latitude: {latitude}, Longitude: {longitude}')

matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

print(f'Matrix: {matrix[1][2]}') # Output: 6

numbers = (1, 2, 3, 4, 5)
for num in numbers:
    print(f'Number: {num}, Type: {type(num)}')

if 7 in numbers:
    print(f'3 is in the tuple.')
else:
    print(f'7 is NOT in the tuple.')

# Slicing Tuple
print(f'Numbers: {numbers[0:4]}')
print(f'Numbers: {numbers[::-1]}')

# Tuple Comprehensions
# Note: There is no such thing as a "tuple comprehension" in Python.
# However, you can create a tuple from a generator expression.

numbers = (1, 2, 3, 4, 5)
gt_three = tuple([num for num in numbers if num > 3])
print(f'Numbers Greater than 3 : {gt_three}')








