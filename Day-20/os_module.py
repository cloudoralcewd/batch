# Working with the OS Module in Python

import os

# Get the current working directory
current_directory = os.getcwd()

print(f"Current Directory: {current_directory}")

# -----------------------------
# 1. Creating a Directory (if it doesn't exist)
# -----------------------------

new_directory = "rns"
if not os.path.exists(new_directory):
    os.mkdir(new_directory)
    print(f"Directory '{new_directory}' created.")
else:
    print(f"Directory '{new_directory}' already exists.")

# -----------------------------
# 2. Checking if a File Exists
# -----------------------------

file_name = "example.txt"
if os.path.isfile(file_name):
    print(f"File '{file_name}' exists.")
else:
    print(f"File '{file_name}' does not exist.")

# -----------------------------
# 3. Listing Directory Contents
# -----------------------------

print("Contents of the current directory:")
for item in os.listdir(current_directory):
    print(item)

# -----------------------------
# 4. Changing the Current Directory
# -----------------------------

new_directory = "rns"
try:
    os.chdir(new_directory)
    print(f"Changed current directory to: {os.getcwd()}")
except FileNotFoundError:
    print(f"Directory '{new_directory}' does not exist. Cannot change directory.")

# -----------------------------

# Rename a File or Directory

old_name = "rns"
new_name = "rnstech"
os.chdir("..")  # Move back to the parent directory
if os.path.exists(old_name):
    os.rename(old_name, new_name)
    print(f"Renamed '{old_name}' to '{new_name}'.")
else:
    print(f"'{old_name}' does not exist. Cannot rename.")





