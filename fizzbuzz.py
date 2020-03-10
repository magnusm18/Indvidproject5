def FizzBuzz(number):
    if number % 5 == 0:
        return(print("Buzz"))

    if number % 3 == 0:
        return(print("Fizz"))

    if number % 3 == 0 and number % 5 == 0:
        return(print("FizzBuzz"))

FizzBuzz(15)