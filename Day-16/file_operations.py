# File Operations in Python

# Open the file and Read the content
    # Read the content Line by Line

# Open the file and Writing the content
    # Adding Lines (Overriding)
    # Appending New Line

# File Content Type
    # text based file content UTF-8
    # Binary file content (PDF, Image, Audio, Video) (0 / 1)

# Relative Path
file = open("./config/configuration.txt", "rt")

content = file.read()
print(content)

file.close()
print(file.closed)

print("#" * 100)

# absolute Path
file = open("E:\\workspace\\B5\\Day-16\\config\\configuration.txt", "rt")

content = file.read()
print(content)

file.close()
print(file.closed)

print("#" * 100)

file = open("./config/configuration.txt", "rt")

content = file.read(71)
print(content)

content = file.read(10)
print(content)

print(file.tell())

file.seek(70)
print(file.tell())

content = file.read(4)
print(content)
file.close()

print("#" * 100)

with open("./config/configuration.txt", "rt") as file:
    file.seek(70)
    print(file.tell())

    content = file.read(4)
    print(content)

print(file.closed)

print("#" * 100)

# READING FILES INTO A LIST

with open("./config/configuration.txt", "rt") as file:
    content = file.read().splitlines()
    print(content[3])
    print(content)

print("#" * 100)

# WRITING TO A FILE

with open("./config/new_config.txt", "wt") as file:
    file.write("This is the First Line. \n")
    file.write("This is the Second Line. \n")
    file.write("This is the Third Line. \n")

with open("./config/configuration.txt", "at") as file:
    file.write("\nThis is the First Line. \n")
    file.write("This is the Second Line. \n")
    file.write("This is the Third Line. \n")




