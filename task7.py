def func_print():
    number = int(input("Введи будь-яке число: "))
    if number >= 10:
        return True
    else:
        return False

result = func_print()
print(result)


def raw_answer(value):
    if value >= 10:
        print("Вірно. Число рівне або більше за 10")
    else:
        print("Число не більше за 10 або не рівне 10")

raw_answer(int(input("Введіть будь_яке число: ")))