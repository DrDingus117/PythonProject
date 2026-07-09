## 1. Loop through 1 to 10
## 2. If not devisible by 3 or 5 print the number
## 3. Check if Num is divisible by 3, if so print "Fizz"
## 4. Check if Num is divisible by 5, if so print "Buzz"
## 5. Check if Num is divisible by 3 and 5, if so print "FizzBuzz"


def fizz_buzz(number):
    result: list[str] = []

    for index in range(1, number + 1):
        if index % 3 == 0 and index % 5 == 0:
            result.append("FizzBuzz")
        elif index % 3 == 0:
            result.append("Fizz")
        elif index % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(index))
    return result


def _prompt_number(default: int = 10) -> int:
    while True:
        try:
            raw = input(f"Enter a positive integer (default {default}): ").strip()
            if raw == "":
                return default
            value = int(raw)
            if value < 1:
                raise ValueError
            return value
        except ValueError:
            print("Invalid input. Please enter a positive integer.")


if __name__ == "__main__":
    n = _prompt_number()
    for line in fizz_buzz(n):
        print(line)