## 1. Loop through 1 to 10
## 2. If not devisible by 3 or 5 print the number
## 3. Check if Num is divisible by 3, if so print "Fizz"
## 4. Check if Num is divisible by 5, if so print "Buzz"
## 5. Check if Num is divisible by 3 and 5, if so print "FizzBuzz"


from unittest import result


def fizz_buzz(number):
    results: list[str] = [str(i) for i in range(1, number + 1)]

    for index in range(1, number + 1):
        if index % 3 == 0 and index % 5 == 0:
            results[index - 1] = "FizzBuzz"
        elif index % 3 == 0:
            results[index - 1] = "Fizz"
        elif index % 5 == 0:
            results[index - 1] = "Buzz"
    return results

n = 10
print(fizz_buzz(n))