#Task 1
"""The user types in a number from 1 to 100. If the number
is a multiple of 3 (divisible by 3 without remainder), print the
word Fizz. If the number is a multiple of 5, print the wordBuzz.
If the word is a multiple of 3 and 5, print Fizz Buzz. If the word
is not a multiple of 3 and 5, print the number.
If the user typed in a number out of the range, print an
error message."""


class OutOfBoundsError(Exception):
    def __init__(self, message="Zadali jste číslo mimo rozsah."):
        self.message = message
        super().__init__(self.message)


while True:
    try:
        number = int(input("Zadejte číslo 0-100:"))
        if number not in range(0, 101):
            raise OutOfBoundsError

        if number % 3 == 0 and number % 5 == 0:
            print("Fizz Buzz")

        elif number % 3 == 0:
            print("Fizz")

        elif number % 5 == 0:
            print("Buzz")

        else:
            print(number)

    except ValueError:
        print("Zadali jste neplatné číslo.")

    except OutOfBoundsError as e:
        print(e.message)