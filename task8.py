def func_calculate(value):
    def wrapper():
        a = int(input("Введи перше число: "))
        b = int(input("Введи друге число: "))
        c = int(input("Введи третє число: "))

        D = b**2 - 4*a*c

        if type(a) == complex:
            a = 0
        elif type(b) == complex:
            b = 0
        elif type(c) == complex:
            c = 0


        value(D)

    return wrapper


@func_calculate
def discriminant(D):
    print(f"Дискримінант рівний: {D}")

discriminant()
