last_name = input("Введіть прізвище: ")
name = input("Введіть ім'я: ")
second_name = input("Введіть по батькові: ")

# Перевірка на пустий рядок для кожної введеної змінної
if len(last_name) == 0 or len(name) == 0 or len(second_name) == 0:
    print("Не введений ключовий параметр")
else:
    # Формування рядка з прізвищем та ініціалами
    initials = "{}. {}.".format(name[0].upper(), second_name[0].upper())

    # Виведення результату на екран
    print("Прізвище та ініціали:", last_name.capitalize(), initials)





# n = int(input("Введіть значення: "))

# # Створення словника
# squares = {}
# for i in range(n + 1):
#   squares[i] = i**2

# # Виведення словника
# print("Створений словник:", squares)


# str_set = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}

# # Отримання значення від користувача
# value = input("Введіть значення: ")

# # Перевірка наявності значення в множині
# if value in str_set:
#   # Видалення значення з множини
#     str_set.remove(value)
#   # Виведення модифікованої множини
#     print(str_set)
# else:
#   # Повідомлення про відсутність значення
#     print(str_set)



# value = input("Введіть елемент ") 
# digits_tuple = (1, 2, 3) 

# # your code goes here
# tuple2 = (value,)
# new = tuple2 + digits_tuple

# print(new)
