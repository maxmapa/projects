count = float(input('Введіть кількість: '))
tariff = 7.80
price = count * tariff
print(price)
cash = float(input('Введіть готівку: '))
rest = cash - price
print("Решта:", round(rest, 2))
