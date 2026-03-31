# FUNCTION ARGUMENTS

# 5 TYPES OF FUNCTION ARGUMENTS:

# 4. USING *args (ARBITRARY POSITIONAL ARGUMENTS)

def calculate_total_cost(base_cost, *items):
    """Calculates the total cost by adding additional variable costs."""
    print(items)
    total_cost = base_cost + sum(items)
    return total_cost

total = calculate_total_cost(100, 20, 30, 50, 100)
print(f'Total Cost: {total}')

print(calculate_total_cost(5))

def create_hashtags(*tags):
    """Creates hashtags based on tags."""
    return ' '.join(tags)

print(create_hashtags('Python', 'Programming', 'Coding'))

# 5. USING **kwargs (ARBITRARY KEYWORD ARGUMENTS)

def display_user_info(**user_data):
    """Displays user information using keyword arguments."""
    for key, value in user_data.items():
        print(f'{key}: {value}')

display_user_info(name='Alice', age=30, city='New York')