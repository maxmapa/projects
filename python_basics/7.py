# number = int(input("Введіть число"))

# # your code goes here
# def print_numbers(number):
#   for i in range(0, number+1,2):
#     print(i)

# print_numbers(number)

# sum = 0
# add = 1
# for i in range(1, 30):
#     sum = sum + add
#     add = 2 * add
# print(sum)

# result = sum(range(1, 31))
# print(result)

# import time
# b=int(input("Введіть початкове значення: "))
# f=1
# for i in range(1,b+1,1):
#    f=f*i
#    time.sleep(0.5) #Зачекати 0,5 секунди
# print(f)

# # Виклик функції та виведення результату
# print("Максимальне число: ", cylinder_volume)

# def year_check(year):
#   if ((year % 4 == 0 and year % 100 != 0)) or (year % 400 == 0):
#     print("True")
#   else:
#     print("False")

# n = int(input("Введіть число: "))
# year_check(n)

# def sieve_of_eratosthenes(n):
#   primes = [True] * (n + 1)
#   primes[0] = primes[1] = False

#   p = 2
#   while p * p <= n:
#       if primes[p]:
#           for i in range(p * p, n + 1, p):
#               primes[i] = False
#       p += 1

#   result = []
#   for i in range(2, n + 1):
#       if primes[i]:
#           result.append(i)

#   return result

# # Приклад використання:
# n = int(input("Введіть число: "))
# print("Прості числа до", n, ":", sieve_of_eratosthenes(n))

# age = int(input("Введіть вік: "))
# if age % 2 == 0:
#   start = 0
# else:
#   start = 1

# # for i in range(start,age+1,2):
# #   print(i)
# ## or option with while
# i=start
# while i <= age:
#   print(i)
#   i = i + 2

# count = 0
# weight = float(input("Введіть вагу машини: "))
# real_weight = weight

# while real_weight <= 100:
#     weight = float(input("Введіть вагу машини: "))
#     real_weight += weight
#     count += 1
# print("Кількість машин, які прибули на склад до його заповнення:", count)

# n = int(input("Введіть кількість навчальних предметів: "))
# avg = 0

# for i in range(n):
#     i = i + 1
#     mark = float(input("Введіть оцінку з предмету " + str(i) + ": "))
#     avg += mark

# avg = avg / n

# print("Середня оцінка:", avg)

# a = 5
# b = 12
# c = 4

# while a <= b:
#     if a % c == 0:
#         print(a)
#     a += 1

# depo = float(input("Введіть суму депозиту: "))
# rate = float(input("Введіть відсоткову ставку: "))
# capital = float(input("Введіть бажану суму капіталу: "))

# period = 0
# while depo < capital: # condition
#    depo = depo + depo * (rate / 100) # depo update
#    period = period + 1  # duration increase

# print("Капітал вийде через", period, "років")

# sum = 0
# add = 1
# for i in range(1, 165):
#     sum = sum + add
#     add = 2 * add
# print(sum)
