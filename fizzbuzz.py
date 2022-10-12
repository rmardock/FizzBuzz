iteration = 0
fizzbuzz = 0
def buzz(fizzbuzz):
    if fizzbuzz %3 == 0 and fizzbuzz %5 == 0:
        print("FizzBuzz")
        return
    if fizzbuzz %3 == 0:
        print("Fizz")
        return
    if fizzbuzz %5 == 0:
        print("Buzz")
        return
    else:
        print(fizzbuzz)
        return
while iteration < 100:
    iteration += 1
    fizzbuzz += 1
    buzz(fizzbuzz)