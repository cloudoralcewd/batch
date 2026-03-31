# While Loops

#while condition:
    # Stmts to execute as long as condition is True

temperature = 70

while temperature < 80:
    print(f'Temperature is {temperature}°F, which is below the threshold.')
    temperature = temperature + 2

# Smart looping techniques: continue, pass, break

sentence = 'AI is the future of technology.'.split()
print(type(sentence))

for word in sentence:
    if word.lower() in ['the', 'is', 'of']:
        continue  # Skip the rest of the loop for this iteration
    print(word)

for num in range(1, 101):
    if num % 10 != 0:
        continue
    print(num)

while True:
    prompt = input("Enter a prompt for the model: ")
    if len(prompt) < 5:
        print("Prompt is too short, please enter at least 5 characters.")
        continue
    else:
        print(f"Generating response for: {prompt}")
        break

# pass - A null operation.
# It is used when a statement is required syntactically, but you do not want to execute any commands or code.
# It's often used as a placeholder.

for model in range(1, 6):
    pass

# THE break STATEMENT

keywords = ['innovation', 'deep learning', 'AI revolution', 'neural networks', 'machine learning']

if 'AI revolution' in keywords:
    print("Keyword found: AI revolution")

for word in keywords:
    if word == 'AI revolution':
        print("Keyword found: AI revolution")
        break

for i in range(3):
    for j in range(3):
        if j == 1:
            break
        print(f'i: {i}, j: {j}')