# Iterations

# 3 Arguments: 1. Start, Increment(step), Condition

# Types of loops:
# 1. For loops - iterate over sequences (lists, tuples, strings, dictionaries, etc.)

# for item in collection:
#       stmts

# 2. While loops - execute as long as a condition is True

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(f'Number - {num}')

tweets = [
    'Exploring AI applications',
    'Machine Learning is the future',
    'Having lunch with friends',
    'New advances in GenAI'
]

for tweet in tweets:
    if 'AI' in tweet or 'Machine Learning' in tweet:
        print (tweet)

feedback = [
    'Great service!',
    'EXCellent response time',
    'Had to wait too long',
    'Excellent support from staff'
]

for fb in feedback:
    if 'excellent' in fb.lower():
        print (fb)

temperature_readings = [71, 74, 78, 82, 85, 90]
threshold = 80

for temp in temperature_readings:
    if temp > threshold:
        print(f'Warning: Temperature exceeded safe limit at {temp}°F')




