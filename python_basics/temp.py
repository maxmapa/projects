#Тиждень 2 / Модуль 5. Алгоритми з розгалуженням / Задача 6.
#Варіант 1
temp = int(input("Введіть Температуру: "))
if temp <= 0:
  res = "A cold, isn’t it?"
if temp < 10:
  res = "Cool"
else:
  res = "Nice weather we’re having"

print(res)

#Варіант 2 (більш елегантний, імхо)
temp = int(input("Введіть Температуру: "))
if temp <= 0:
  res = "A cold, isn’t it?"
elif temp < 10:
  res = "Cool"
else:
  res = "Nice weather we’re having"

print(res)
#Тут використано конструкцію elif для того, щоб перевірити умови лише у випадку, якщо попередня умова не виконана.

t = int(input("Введіть число: "))

if t <= 0:
  message = "Лід"
elif t < 100:
  message = "Вода"
else:
  message = "Пара"

print(message)
