# COMMON STRING METHODS

model_output = 'ai IS the future of everything!'

print(model_output)
print(model_output.upper())
print(model_output.lower())
print(model_output.title())
print(model_output.capitalize())

# STRING STRIPPING
response = ' ?? Hello, human! ?? '

print(response)
print(response.strip())
print(response.strip(' ??'))

text = 'ML is a critical component of modern AI. ML techniques are advancing rapidly.'
print(text)
# print(id(text))
print(text.replace('ML', 'Machine Learning'))

text = 'AI is the FUture. Embrace the future of AI!'
print(text.lower().count('future'))

# STRING SPLITTING
statement = 'AI breakthrough, at every step'
words = statement.split()
print(words)
print(type(words))

# STRING JOINING
terms = ['AI', 'ML', 'GenAI', 'LLM', 'NLP']
print(type(terms))

# Join the list elements into a single string, separated by ', '
ml_words =', '.join(terms)
print(ml_words)

# Remove 'https://' from the beginning of the URL
url = 'https://example.com'

domain_url = url.removeprefix('https://')
print(domain_url)

domain = domain_url.removesuffix('.com')
print(domain)

'''
upper
lower
title
capitalize
strip
replace
count
split - String to list
join - List to string
removeprefix
removesuffix
'''








