import time


def CheckNumbers(param):
    while True:
        try:
            number = int(input(f"{param}\n"))
            if number > 0:
                return number
            else:
                print("Число введено неправильно.")
        except:
            print("Число введено неправильно.")


number = CheckNumbers("Сколько рядов у ёлки?")
print("Ёлочка, зажгись!\n")
time.sleep(0.7)
for i in range(number):
    time.sleep(0.3)
    print((number - i) * " ", (2 * (i + 1) * "*")[:-1], sep="")
