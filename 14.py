s = input("Введите число: ")
while not s.isdigit():
    print("Ошибка. Попробуйте еще раз.", end=" ")
    s = input("Введите число: ")
print("Введено целое число:", s)
