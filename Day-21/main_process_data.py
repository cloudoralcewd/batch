
from process_data import clean_data, tokenize_text

new_text = "   Hello, World! This is a test.   "
cleaned = clean_data(new_text)
print("Cleaned Text:", cleaned)

tokens = tokenize_text(cleaned)
print("Tokens:", tokens)

# csv, json, os, sys, random, requests

# Django - web framework
# Flask - web framework