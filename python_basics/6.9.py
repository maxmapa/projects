# option 1 Sorted
number = input("Введіть число: ")

digits = sorted(number, reverse=True)
for digit in digits:
    print(digit)
print()
digits = sorted(number, reverse=False)
for digit in digits:
    print(digit)

# option 2 
number = input("Введіть число: ")

for digit in number:
    print(digit)
print()
for digit in reversed(number):
  print(digit)