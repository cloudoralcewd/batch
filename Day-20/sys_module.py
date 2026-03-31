# input() - manually input data

# sys.argv - command line arguments
# sys.exit() - exit the program

import sys

help(sys.argv)

# print python version
print("Python version:", sys.version)



# print command line arguments
print("Command line arguments:", sys.argv)

print("First Argument", sys.argv[0])
if len(sys.argv) > 1:
    print("Second Argument", sys.argv[1])
if len(sys.argv) > 2:
     print("Third Argument", sys.argv[2])

sys.exit()

for i in range(1, len(sys.argv)):
    print(f"Argument {i}: {sys.argv[i]}")






