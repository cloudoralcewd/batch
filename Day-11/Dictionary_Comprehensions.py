# [expression for n in nums if condition]

# Dictionary Comprehensions

names = {'alice', 'BOB', 'charlie', 'DAVE'}

capital = {name.capitalize() for name  in names}
print(f'Capitalized Names: {capital}')

hyperparams = {'layers': 3, 'units': 256, 'dropout': 0.2}

new_dict = {key: val * 2 for key, val in hyperparams.items()}
print(new_dict)

sales = {2022: 50000, 2023: 75000, 2024: 100000}

profit = {year: amount * (15/100) for year, amount in sales.items()}
print(profit)

years = [2020, 2021, 2022]
dataset_sizes = [10000, 25000, 50000]

print(dict(zip(years, dataset_sizes)))

# Integer, String, Float, Boolean
# List, Tuple, Set, Frozenset, Dictionary









