import json

lst = []

def saver():
    with open("operations.txt", "wt") as file:
        json.dump(lst, file)

def history():
    with open("operations.txt", "rt") as file:
        obj = json.load(file)
    print(obj)

def summ():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    result = a + b
    lst.append([a, "+", b, "=", result])
    print(a, "+", b, "=", result)


def sub():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    result = a - b
    lst.append([a, "-", b, "=", result])
    print(a, "-", b, "=", result)


def mul():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    result = a * b
    lst.append([a, "*", b, "=", result])
    print(a, "*", b, "=", result)


def div():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    try:
        result = a / b
        lst.append([a, "/", b, "=", result])
        print(a, "/", b, "=", result)
    except ZeroDivisionError as  exception:
        print("Деление на ноль невозможно!")

def exp():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    result = a ** b
    lst.append([a, "**", b, "=", result])
    print(a, "**", b, "=", result)
