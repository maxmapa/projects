import time

n = int(input("Введіть початкове значення: "))

while n >= 1:
  print(n)
  time.sleep(1)  # Почекати 1 секунду
  n = n - 1

print("Start")
