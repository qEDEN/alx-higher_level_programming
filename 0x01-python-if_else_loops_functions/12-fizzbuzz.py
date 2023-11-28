#!/usr/bin/python3
def fizzbuzz():
    """
    Prints numbers from 1 to 100, replacing multiples of three with Fizz,
    multiples of five with Buzz, and multiples of both three and five with FizzBuzz.
    """
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")

# Test the fizzbuzz function
fizzbuzz()
print("")
