input_database_name = input("Введіть ім'я бази даних ")
input_command_to_execute = input("Введіть команду для виконання ")

class Database:
# your code goes here
  executed_commands = []  # Визначаємо як атрибут класу

  def __init__(self, database_name):
      self.database_name = database_name
      self.connected_to_database = False

  @staticmethod
  def to_lower(str):
      return f"{str.lower()}"

  def add_to_executed_commands(self, command):
      Database.executed_commands.append(command)  # Користуємось атрибутом класу

  def connect_to_database(self):
      self.connected_to_database = True
      print("Під'єднано до бази даних")  

  @classmethod
  def execute_command(cls, command):  # Додаємо параметр command
      cls.executed_commands.append(command)
      print(command)

# your code goes here
db = Database(input_database_name)
print(db.database_name)
print(db.connected_to_database)

db.connect_to_database()
print(db.connected_to_database)
print(Database.executed_commands)

lower_command = Database.to_lower(input_command_to_execute)
db.execute_command(lower_command)
print(Database.executed_commands)


# name = input("Введіть ім'я користувача  ")
# new_name = input("Введіть нове ім'я користувача ")
# new_last_name = input("Введіть нове прізвище користувача ")
# new_second_name = input("Введіть нове по батькові користувача ")

# class User:
#   count_users = 0

# # your code goes here
#   def __init__(self, name):
#     self.name = name  # Зберігає ім'я користувача
#     User.count_users += 1  # Збільшує лічильник користувачів при створенні нового об'єкту

#   def change_username(self, username):
#     self.name = username  # Змінює ім'я користувача

#   @classmethod
#   def get_count(cls):
#     print("Кількість користувачів:", cls.count_users)  # Виводить кількість користувачів на екран

#   @staticmethod
#   def prepare_name(name, last_name, second_name):
#       return f"{last_name} {name[0]}.{second_name[0]}."

# new_username = User.prepare_name(new_name, new_last_name, new_second_name)

# user1 = User(name)
# print(user1.name)
# print(User.count_users)
# print(user1.count_users)
# user1.change_username(new_username)
# print(user1.name)

# user2 = User(name)
# print(User.count_users)
# print(user2.count_users)


# input_sentence = input("Введіть речення: ")
# sentence_to_compare = input("Введіть речення для порівняння: ")
# new_word = input("Введіть нове слово, яке потрібно додати в кінець речення: ")
# input_word_to_remove = input("Введіть слово яке потрібно вилучити: ")

# class Sentence:
#   def __init__(self, sentence):
#     self.sentence = sentence
#     self.original_sentence = sentence  # Зберігає оригінальне речення

#   def to_lower(self):
#     self.sentence = self.sentence.lower()

#   def is_similar(self, sentence_to_compare):
#     return self.original_sentence.lower() == sentence_to_compare.lower()

#   def add_word(self, word_to_add):
#     self.sentence += word_to_add

#   def remove_word(self, word_to_remove):
#     self.sentence = self.sentence.replace(word_to_remove, "")

# my_sentence = Sentence(input_sentence)
# print(my_sentence.is_similar(sentence_to_compare))

# my_sentence.add_word(new_word)
# my_sentence.to_lower()
# print(my_sentence.sentence)

# my_sentence.remove_word(input_word_to_remove)
# print(my_sentence.sentence)



# wheels_count = int(input("Введіть кількість коліс "))
# sits = int(input("Введіть кількість місць "))
# guns_count = int(input("Введіть кількість зброї "))

# class Banderomobil:
# # your code goes here
#   cars_count = 0
#   def __init__(self, wheels_count, sits, guns_count):
#     self.wheels_count = wheels_count
#     self.sits = sits
#     self.guns_count = guns_count
#     Banderomobil.cars_count += 1
#   def print_info(self):
#     print("Бандеромобіль на {} колесах, призначений для {} людей і {} стволів".format(self.wheels_count, self.sits, self.guns_count))

# car1 = Banderomobil(wheels_count, sits, guns_count )
# car1.print_info()
# print(car1.cars_count)

# car2 = Banderomobil(wheels_count+1, sits+1, guns_count+1 )
# car2.print_info()
# print(car2.cars_count)


# car_1 = input("Введіть марку автомобіля 1 ")
# car_2 = input("Введіть марку автомобіля 2 ")
# car_3 = input("Введіть марку автомобіля 3 ")

# class Cars:
# # your code goes here
#   list_of_cars = []
# Cars.list_of_cars.append(car_1)
# Cars.list_of_cars.append(car_2)
# Cars.list_of_cars.append(car_3)
# cars_string = " та ".join(Cars.list_of_cars)
# print("Список авто: {}".format(cars_string))


# windows_count = int(input("Введіть кількість вікон "))
# flors_count = int(input("Введіть кількість поверхів "))

# class Building:
# # your code goes here
#   windows_count = 0
#   flors_count = 0

# Building.windows_count = windows_count
# Building.flors_count = flors_count

# print("Загальна кількість вікон {}".format(Building.windows_count * Building.flors_count))