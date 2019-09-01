from Calculator.operations import summ, sub, mul, div, exp, saver, history

ask = 0
while ask != "Q":
    ask = int(input("""
Введите номер действия:
1. Сложение
2. Вычитание
3. Умножение
4. Деление
5. Возведение в степень
6. Вывод сохраненных результатов
Выход - Q
"""))

    if ask == 1:
        summ()
        saver()
    elif ask == 2:
        sub()
        saver()
    elif ask == 3:
        mul()
        saver()
    elif ask == 4:
        div()
        saver()
    elif ask == 5:
        exp()
        saver()
    elif ask == 6:
        history()
