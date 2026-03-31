# STRING CONCATENATION (LESS EFFICIENT)

model_name = 'GPT'
version = 4
msg = 'Hello'

print(msg + ' from ' + model_name + ' version ' + str(version) + '!')

# USING F-STRINGS (MORE READABLE & EFFICIENT)
print(f'{msg} from {model_name} version {version}!')

# FORMATTING NUMBERS WITH F-STRINGS
token_used = 123
cost_per_token = 0.001

total_cost = token_used * cost_per_token
print(f'Total cost: {total_cost:.5f}')

