def fizz_buzz(n: int) -> None:
    for i in range(1, n + 1):
        if i % 15 == 0:          # делится и на 3, и на 5
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

