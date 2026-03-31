
def clean_data(text):
    # Remove leading and trailing whitespace
    cleaned_text = text.strip()

    return cleaned_text.lower()

def tokenize_text(text):
    # Split the text into words
    tokens = text.split()
    return tokens

if __name__ == '__main__':
    sample_text = "   Hello, World! This is a test.   "
    cleaned = clean_data(sample_text)
    print("Cleaned Text:", cleaned)

    tokens = tokenize_text(cleaned)
    print("Tokens:", tokens)
