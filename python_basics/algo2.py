count = int(input('Введіть кількість: '))
tariff = 7.80
price = count * tariff
print(price)
cash = int(input('Введіть готівку: '))
rest = cash - price
print(rest)
