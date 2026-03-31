# List Basics

# List is a collection which is ordered and changeable. Allows duplicate members.

# # Empty List
# empty_list1 = []
# empty_list2 = list()
# print(f'Empty List 1: {empty_list1}')
# print(f'Empty List 2: {empty_list2}')

sample_list = [42, 32.15, "Hello", True]
print(sample_list)
print(f'Length of the list: {len(sample_list)}')

# # Accessing List Elements
print(f'3rd element: {sample_list[2]}')
print(f'Last element: {sample_list[-1]}')

# List - mutable
print(f'Memory reference before modification: {id(sample_list)}')
sample_list[1] = 50.0
print(f'Memory reference after modification: {id(sample_list)}')

sample_list[-1] = False
print(f'List after modification: {sample_list}')

# Adding an element to the list
sample_list.append(1000)
print(f'List after modification: {sample_list}')
sample_list.append(["How are you", True])
print(f'List after modification: {sample_list}')

print(f'Nested list element: {sample_list[5][1]}')

sample_list.append("NLP")
sample_list.append("LLMs")
print(f'List after modification: {sample_list}')
print(f'Length of the list: {len(sample_list)}')

# Nested lists (2D lists)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9, [10, 11, 12]]
]

print(matrix[1][1]) # Output: 5
print(matrix[2][2]) # Output: 9
print(matrix[2][3][1]) # Output: 11








