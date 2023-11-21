for i in range(1, 101):
    message = ""

    if i % 3 == 0:
        message += "Fizz"

    if i % 5 == 0:
        message += "Buzz"

    if not message:
        message = i

    if i % 3 == 0 and i % 5 == 0:
        message = "FizzBuzz"

    print(message)