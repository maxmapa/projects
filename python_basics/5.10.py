a = int(input("Задайте a: "))
b = int(input("Задайте b: "))
c = int(input("Задайте c: "))
count = 0

if a == b or a == c:
  count += 1
if b == c:
  count += 1

print(count)
