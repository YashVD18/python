#Task1
# Program to calculate factorial using a function (loop method)

# Step 1: Define function
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# Step 2 & 3: Call function and print output
num = 5   # sample number
print("Factorial of", num, "is:", factorial(num))

#Task2
# Program to calculate sqrt, log, and sine using math module
import math

# Step 1: Take user input
num = float(input("Enter a number: "))

# Step 2: Perform calculations
sqrt_value = math.sqrt(num)           # square root
log_value = math.log(num)             # natural log (base e)
sine_value = math.sin(num)            # sine in radians

# Step 3: Display results
print("Square root of", num, "=", sqrt_value)
print("Natural log of", num, "=", log_value)
print("Sine of", num, "=", sine_value)


