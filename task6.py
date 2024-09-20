price = int(input('Введіть суму для оплати: '))
def payment_cash_dask(m, *prices):
    total_bills = 0

    for price in prices:
        if m >= price:
            total_bills += m // price
            m %= price

    if m > 0:
        print(f"Неможливо оплатити даними куп'юрами")
    else:
        print(f"Мінімальна к-сть купюр для оплати: {total_bills}")

payment_cash_dask(price, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1)
