# VARIABLE SCOPE AND NAMESPACES

scores = [85, 90, 78, 92, 88]

print(scores)

accuracy = 0.95 # Global variable

def report_accuracy():
    print(f"Model accuracy is: {accuracy * 100}%")

report_accuracy()
print(accuracy)

def count_tokens(text):
    token_count = len(text.split()) # Local variable
    return token_count

print(count_tokens("This is a sample text for token counting."))

accuracy = 0.85

print(accuracy)

def update_accuracy():
    global accuracy
    accuracy = 0.90
    print(f"Updated accuracy inside function: {accuracy * 100}%")

update_accuracy()
print(accuracy)
