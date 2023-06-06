def CheckNumbers(param):
    while True:
        try:
            number = int(input(f"{param} "))
            if 100000 >= number > 0:
                return number
            else:
                print("Число введено неправильно.")
        except:
            print("Число введено неправильно.")


def SimpleOrComplex(number):
    check = False
    for i in range(2, number):
        if number % i == 0:
            check = True
            break
    if check == False:
        print(f"Число {number} простое.")
    else:
        print(f"Число {number} составное.")


number = CheckNumbers("Введите любое натуральное число до 100000:")
if number == 1:
    print("Число 1 простое.")
else:
    SimpleOrComplex(number)
