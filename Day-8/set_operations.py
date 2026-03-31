# Sets basics

# mutable, un-ordered, no duplicates
# {}

unique_ids = {1, 2, 3, 3, 'a', 'b', 4}
print(f'Set of unique IDs: {unique_ids}')
print(f'Length of the set: {len(unique_ids)}')

# empty set
# empty_set = {}
empty_set = set()
print(f'Empty set Type : {type(empty_set)}')

sentences = ['Hello world', 'AI is amazing', 'Hello world', 'Python is great']
unique_sentences = set(sentences)
print(f'Unique sentences: {list(unique_sentences)}')

unique_ids = {1, 2, 3, 3, 'a', 'b', 4}
# Adding elements to a set
unique_ids.add(10)
unique_ids.add(1)
print(f'Set after adding an element: {unique_ids}')

unique_ids.remove('a')
print(f'Set after removing an element: {unique_ids}')

# print(unique_ids[3])

for item in unique_ids:
    print(f'Item: {item}, Type: {type(item)}')

item = 'a'

if item in unique_ids:
    print(f'{item} is in the set.')
else:
    print(f'{item} is NOT in the set.')

# immutable, unique values, un-ordered collection
frozen_set_example = frozenset([1, 2, 3, 4, 4, 5])
print(f'Frozen set example: {frozen_set_example}')
print(f'Frozen set example: {type(frozen_set_example)}')
