# ESSENTIAL LIST METHODS IN PYTHON

# 1. append() - Adds an element to the end of the list

my_list = []
my_list.append(10)
my_list.append(20)
print(my_list)

# 2. extend(): Extends the list with elements from an iterable
my_list.extend([40, 50])
print(my_list)
print(len(my_list))

# 3. insert(): Inserts an element at a specified position
my_list.insert(2, 30)
print(my_list)
print(len(my_list))

# 4. remove(): Removes the first occurrence of a specified value
# my_list.remove(20)
# print(my_list)

# 5. pop(): Removes and returns an element at a specified index (default is the last element)
last_element = my_list.pop()
print(last_element)

# 6. pop(2) # removes the element at index
removed_element = my_list.pop(1)

# 5. clear(): Removes all elements from the list
# my_list.clear()
print(my_list)

# List Slicing and Methods
# [start_index:stop_position:step]

numbers = [1, 2, 3, 4, 5]

# Output: [2, 3, 4]
print(numbers[1:4])

# Output: [1, 2, 3]
print(numbers[:3])

# Output: [3, 4, 5]
print(numbers[2:])

# Output: [2, 4]
print(numbers[1::2])

# Output: [5, 4, 3, 2, 1]
print(numbers[::-1])

# REVERSING AND SORTING LISTS
# reverse(): Reverses the order of elements in place
sequence = [1, 2, 3, 4, 10, 100, 1000, 'Hello']
sequence.reverse()
print(sequence)

# sort(): Sorts the list in ascending order (default)
numbers = [3, 1, 4, 1, 5]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)




# append
# extend
# insert
# remove
# clear
# pop
# reverse
# sort




