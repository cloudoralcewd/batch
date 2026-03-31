# DICTIONARY BASICS

# List - []
# Tuple - ()
# Set - {}
# Dictionary - {key: value}

# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
model_config = {
                    'model_name': 'gpt-3.5-turbo',
                    'layers': 100,
                    'parameters': '250B',
                     10: 'Ten',
                    True: 'Active',
                    (1,2): 'Tuple Key'
                }
print(f'Model Config: {model_config}')
print(f'Type of model_config: {type(model_config)}')
print(f'Length of model_config: {len(model_config)}')

hyperparameters = {
    'learning_rate': 0.0001,
    'dropout_rate': 0.3,
    'optimizer': 'Adam',
    'learning_rate': 0.0004,
}

print(hyperparameters)

# Accessing dictionary values using keys

print(f'{hyperparameters['optimizer']}')
print(f'{hyperparameters['learning_rate']}')

print(f'{hyperparameters.get('opmizer', 'Key not found')}')

hyperparameters['dropout_rate'] = 0.2
hyperparameters['batchsize'] = 32

hyperparameters['batchsize'] = 64

print(f'Updated Hyperparameters: {hyperparameters}')

# BEST PRACTICES FOR DICTIONARIES

# 1. Stick to **immutable keys** (e.g., strings, numbers, tuples, Booleans) to ensure data integrity and avoid unexpected behavior.
# 2. Avoid **duplicate keys** (last assigned value will override)
# 3. Use **.get()** for safe access to prevent errors

# NESTED DICTIONARIES

pipeline_config = {
    'GPT-4': {
            'layers': 48,
            'parameters': '175B',
            'attention_heads': 96
    },
    'Gemini': {
            'layers': 64,
            'parameters': '200B',
            'attention_heads': 128
    },
     'LLaMA': {
            'layers': 32,
            'parameters': '70B',
            'attention_heads': 64
     }
}

print(pipeline_config['Gemini']['parameters'])
print(pipeline_config['LLaMA']['attention_heads'])

print(pipeline_config.get('Gemini').get('parameters'))
print(pipeline_config.get('LLaMA').get('attention_heads'))




