# DICTIONARY OPERATIONS AND METHODS: ACCESSING, UPDATING, .GET(), .KEYS(), AND .VALUES()

# ASSIGNMENT AND COPYING

model_params = {'layers': 24, 'units': 512, 'activation': 'relu'}

print(f'Original Model Parameters: {model_params}')
print(f'Length: {len(model_params)}')

# Deep Copy
shared_params = model_params
model_params['units'] = 1024
print(f'Updated Model Parameters: {model_params}')
print(f'Shared Parameters: {shared_params}')

shared_params['tokens'] = 2048
print(f'Updated Model Parameters: {model_params}')
print(f'Shared Parameters: {shared_params}')

safe_params = model_params.copy()
print(f'Safe Parameters: {safe_params}')
print(f'Original Model Parameters: {model_params}')

safe_params['dropout'] = 0.3
print(f'Updated Safe Parameters: {safe_params}')
print(f'Original Model Parameters: {model_params}')

# MERGING DICTIONARIES using update() method

base_config = {'batch_size': 32, 'epochs': 10}
version_config = {'learning_rate': 0.001, 'units': 128, 'epochs': 20}

base_config.update(version_config)
print(f'Original Model Parameters: {base_config}')
print(f'Version COnfig: {version_config}')

# Get all keys from base_config
print(f'Keys of the Base Config: {base_config.keys()}')

# Get all values from base_config
print(f'Values of the Base Config: {base_config.values()}')

# Get key and values from base_config
print(f'Key and Values of the Base Config: {base_config.items()}')

for key in base_config.keys():
    print(f'Key: {key}')

for value in base_config.values():
    print(f'Value: {value}')

for item in base_config.items():
    # print(f'Item: {item}')
    print(f'Key: {item[0]}, Value: {item[1]}')

for key, value in base_config.items():
    print(f'Key: {key}, Value: {value}')

print('batch_size' in base_config.keys())
print(100 in base_config.values())

print(('batch_size', 32) in base_config.items())

# Logical AND, logical OR

# Logical AND (and): Returns True if both conditions are true, otherwise returns False.
#    cond1  AND(&)   cond2    result
#      T    AND     F       F
#      F            T       F
#      F            F       F
#      T            T       T

# Logical OR (or): Returns True if at least one condition is true, otherwise returns False.
#    cond1  OR   cond2    result
#      T    OR     F       T
#      F            T       T
#      F            F       F
#      T            T       T

# Find common keys between two dictionaries using set intersection
config_a = {'batch_size': 32, 'optimizer': 'adam'}
config_b = {'batch_size': 64, 'optimizer': 'adam', 'momentum': 0.9}

common_keys = config_a.keys() & config_b.keys()
print(common_keys)

merged_dict = config_a.keys() | config_b.keys()
print(merged_dict)

# CLEARING A DICTIONARY

config_a.clear()
print(f'Cleared Config A: {config_a}')

data = {'name': 'Alice', 'age': 30, 'city': 'New York'}
deleted_item = data.pop('city')
print(f'Deleted Item: {deleted_item}')
print(f'Updated Data: {data}')

last_item = data.popitem()
print(f'Last Item: {last_item}')
print(f'Updated Data: {data}')





