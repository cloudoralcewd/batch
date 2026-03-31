# GETTING USER INPUT

name = input("Enter Your Name: ")
print("Hello, " + name + "! Welcome to the world of AI!")
# print(type(name))

age = input("Enter Your Age: ")
# print(type(age))
print("Your age is - " + age)

training_hours = int(input('Enter hours spent training the model: '))
print("You have spent " + str(training_hours) + " hours training the model.")

iterations = int(input('Enter the number of model iterations (integer): '))
print("The model has been trained for " + str(iterations) + " iterations.")

total = training_hours * iterations
print(total)