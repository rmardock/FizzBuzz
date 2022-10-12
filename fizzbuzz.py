# Challenge: FizzBuzz on GitHub
# Written by Ryan Mardock

# Variables
iteration = 0
fizzbuzz = 0

# FizzBuzz function
def buzz(fizzbuzz):
    # If variable is divisible by both 3 and 5
    if fizzbuzz %3 == 0 and fizzbuzz %5 == 0:
        print("FizzBuzz")
        return
    # If variable is divisible by 3 (only)
    if fizzbuzz %3 == 0:
        print("Fizz")
        return
    # If variable is divisible by 5 (only)
    if fizzbuzz %5 == 0:
        print("Buzz")
        return
    # If variable is not divisible by 3 or 5
    else:
        print(fizzbuzz)
        return
    
# While loop for iterating FizzBuzz function using numbers from 1 to 100
while iteration < 100:
    # Increase iteration variable by 1
    iteration += 1
    # Increase fizzbuzz variable by 1
    fizzbuzz += 1
    # Call FizzBuzz function
    buzz(fizzbuzz)