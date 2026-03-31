# CORE STRING OPERATIONS: INDEXING, SLICING, CONCATENATING

message = 'GenAI is amazing!'
print(message[0])
print(message[3])
print(message[16])
print(message[-1])
print(message[-8])

# STRINGS ARE IMMUTABLE
# message[0] = 'X'

# STRING CONCATENATION
greeting = 'Hello, '
role = 'AI enthusiast'

full_greeting = greeting + role + '!' + ' Welcome to the world of AI.'
print(full_greeting)

print("Version" + str(1.0))

# STRING REPETITION

# * in integer 3 * 4 = 12

separator = '??'
print(separator * 100)

tech = 'Machine Learning'

# string[start_index:stop_position:step]
print(tech[0:7])
print(tech[8:16])
print(tech[8:13])

print(tech[:7])
print(tech[-1:])

# string[start_index:stop_position:step]
print(tech[0:16:3])

print(tech[::-1])





