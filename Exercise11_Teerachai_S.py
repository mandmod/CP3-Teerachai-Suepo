inputNumber = int((input("Input Number : ")))
for i in range(inputNumber):
    print(" " * (inputNumber - i - 1) + ("*" * (2 * i + 1)))
