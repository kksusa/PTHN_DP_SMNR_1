def CheckNumbers(letter):
    while True:
        try:
            number = int(input(f"Введите сторону {letter}: "))
            if number > 0:
                return number
            else:
                print("Число введено неправильно.")
        except:
            print("Число введено неправильно.")


def CheckTriangle(a, b, c):
    if a >= b + c or b >= a + c or c >= a + b:
        print("Такого треугольника не существует.")
    elif a != b and a != c and b != c:
        print("Треугольник разносторонний.")
    elif a == b == c:
        print("Треугольник равносторонний.")
    else:
        print("Треугольник равнобедренный.")


a = CheckNumbers("A")
b = CheckNumbers("B")
c = CheckNumbers("C")
CheckTriangle(a, b, c)
