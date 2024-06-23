def maximum(x, y):
  if x > y:
      max = x
  else:
      max = y

  return max

a = float(input("Введіть число a "))
b = float(input("Введіть число b "))
c = float(input("Введіть число c "))
d = float(input("Введіть число d "))
max1 = maximum(a, b)
max2 = maximum(c, d)
result = maximum(max1, max2)
print("Максимальне значення=", result)