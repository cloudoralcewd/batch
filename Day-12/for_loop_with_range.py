

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Working with Ranges in Python

# -----------------------------
# 1. Using range() in a Loop
# -----------------------------

# range(start, stop) -> stop is exclusive
for i in range(5):
    print(f'index - {i}')

for participant in range(10, 101):
    print(f"Participant: {participant}")

# -----------------------------
# 2. Creating a List from a Range
# -----------------------------

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = list(range(1,11))
print(numbers)

# [start:stop:step]
# [1:]
# [1:5:]

even_numbers = list(range(2, 11, 2))
print(even_numbers)

odd_numbers = list(range(1, 11, 2))
print(odd_numbers)





