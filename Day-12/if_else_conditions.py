# CONDITIONAL STATEMENTS (if ... elif ... else)

"""
if condition1:
    True Stmt 1
elif condition2:
    True Stmt 2
elif  condition3:
    True Stmt 3
elif condition4:
    True Stmt 4
else:
    Stmt 5
"""

temperature = int(input('Enter the temperature in Celsius: '))

if temperature < 0:
    print("1.It's freezing, wear a heavy coat!")
elif temperature < 15:
    print("2.It's chilly! You might need a jacket!")
elif temperature < 25:
    print("3.The weather is mild. A light sweater should be enough.")
else:
    print("4.It's hot! Stay cool and hydrated.")
print("5.Outside of if block")

temperature = 10

if temperature < 15:
    print("It's chilly! You might need a jacket.")
elif temperature < 27:
    print("The weather is mild. A light sweater should be enough.")
else:
    print("It's hot! Stay cool and hydrated.")

