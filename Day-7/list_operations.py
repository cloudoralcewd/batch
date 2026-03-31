# List Operations: Concatenation and Iteration

# -----------------------------
# 1. List Concatenation
# -----------------------------

list_1 = [3, 4]
print(f'List 1: {list_1}, Memory reference: {id(list_1)}')

list_1 = list_1 + [5, 6]    # Creates a new list (concatenation)
print(f'List 1: {list_1}, Memory reference: {id(list_1)}')  # Memory address changes

list_1 += [7, 8]   # Modifies the existing list in place (augmented assignment)
print(f'List 1: {list_1}, Memory reference: {id(list_1)}') # Memory address remains the same

# -------------------------------------
# 2. Iteration and Membership Testing
# ------------------------------------

# print(list_1[0])
# print(list_1[1])
# print(list_1[2])

# ip = ip_list[0]
# ip = ip_list[1]

# Iterating through the list using a for loop
ip_list = ['192.168.0.1', '192.168.0.2', '10.0.0.1', '10.0.0.2']

for ip in ip_list:
    print(ip)

target_ip = ["10.0.0.2", "10.0.0.3"]

for ip_address in target_ip:
    if ip_address in ip_list:
        print(f'{ip_address} is in the list.')
    else:
        print(f'{ip_address} is NOT in the list.')

# Deep Copy vs Shallow Copy

list_a = [1, 2, 3]
print(f'List A: {list_a}, Memory reference: {id(list_a)}')

list_b = list_a
print(f'List B: {list_b}, Memory reference: {id(list_b)}')

list_b.append(4)
print(f'List A: {list_a}, Memory reference: {id(list_a)}')
print(f'List B: {list_b}, Memory reference: {id(list_b)}')

list_a.append(5)
print(f'List A: {list_a}, Memory reference: {id(list_a)}')
print(f'List B: {list_b}, Memory reference: {id(list_b)}')

# To avoid this, use list.copy() for a shallow copy
list_c = list_a.copy()
print(f'List A: {list_a}, Memory reference: {id(list_a)}')
print(f'List C: {list_c}, Memory reference: {id(list_c)}')

list_c.append(6)
print(f'List A: {list_a}, Memory reference: {id(list_a)}')
print(f'List C: {list_c}, Memory reference: {id(list_c)}')

list_b.append(7)
print(f'List A: {list_a}, Memory reference: {id(list_a)}')
print(f'List B: {list_b}, Memory reference: {id(list_b)}')
print(f'List C: {list_c}, Memory reference: {id(list_c)}')

# List Comprehensions
nums = [1, 2, 3, 4, 5, 6, 7]
#
# new_list = []
#
# for num in nums:
#     if num > 5:
#         new_list.append(num)
# print(new_list)

# [expression for item in list if condition]
new_list = [num for num in nums if num >= 5]
print(new_list)

contributors = ['alice', 'Bob', 'CHARLIE']
con_name_cap = [name.capitalize() for name in contributors]
print(con_name_cap)

nums = [1, 7, 8, 14, 21, 30, 50]
nums_divide_by_7 = [num for num in nums if num % 7 == 0]
print(nums_divide_by_7)

ai_team = ['Alice', 'Bob', 'Charlie']
data_team = ['Alice', 'David', 'Charlie']
common_team = [name for name in ai_team if name in data_team]
print(f"Common members in AI and Data teams: {common_team}")

