input_qa_name= input("Введіть ім'я тестувальника: ")
input_pm_name = input("Введіть нове ім'я менеджера: ")
input_qa_expected_action = input("Введіть очікувану дію для тестувальника: ")
input_pm_expected_action = input("Введіть очікувану дію для менеджера: ")
input_qa_task = input("Введіть поставлену задачу тестувальнику: ")

# your code goes here
class User:
  def __init__(self, username, expected_action):
    self._username = username
    self._expeted_action = expected_action

  def perform_action(self):
    print("{} виконує дію: '{}'".format(self._username, self._expeted_action))

  def get_username(self):
    return self._username
  def set_username(self, value):
    self._username = value.title()
    
class QA(User):
  def __init__ (self, username, expected_action, tasks=[]):
    super().__init__(username, expected_action)
    self.tasks = tasks
  def set_task(self, task):
    self.tasks.append(task)  

class Manager(User):
  def __init__ (self, username, expected_action):
    super().__init__(username, expected_action)
  def perform_action(self):
    print("Зайнятий. Напишіть мені листа з Вашим питанням")
  

  
qa = QA(input_qa_name, input_qa_expected_action)
print(qa.get_username())
qa.set_username(input_qa_name)
print(qa.get_username())
qa.perform_action()
print(qa.tasks)
qa.set_task(input_qa_task)
print(qa.tasks)

pm = Manager(input_pm_name, input_pm_expected_action)
print(pm.get_username())
pm.set_username(input_pm_name)
print(pm.get_username())
pm.perform_action()


# input_database_name = input("Введіть ім'я бази даних ")
# new_database_name  = input("Введіть нове ім'я бази даних ")

# class Database:
#    # your code goes here
#   def __init__(self, database_name):
#     self.__database_name = database_name
#     self._connected_to_database = False

#   def get_connected_to_database(self):
#     return self._connected_to_database
#   def set_connected_to_database(self, connection_state):
#     self._connected_to_database = connection_state
#     print("Неможливо змінити значення connected_to_database за допомогою присвоєння. Використайте метод connect_to_database")

#   def get_database_name(self):
#     return self.__database_name
#   def set_database_name(self, value):
#     self.__database_name = value.upper()
#     value = new_database_name
    
#   def connect_to_database(self):
#     self._connected_to_database = True
#     print("Під'єднано до бази даних")

# db = Database(input_database_name)
# print(db._connected_to_database)
# print(db.get_connected_to_database())
# db.set_connected_to_database(True)

# db.connect_to_database()
# print(db._connected_to_database)
# print(db.get_connected_to_database())

# print(db.get_database_name())
# db.set_database_name(new_database_name)
# print(db.get_database_name())
