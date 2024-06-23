a = float(input("Side A:? "))
b = float(input("Side B:? "))
c = float(input("Side C:? "))
perimeter = a + b + c
print("Perimeter =", perimeter)

a = int(input("Side A:? "))
b = int(input("Side B:? "))
c = int(input("Side C:? "))
perimeter = a + b + c
print("Perimeter =", perimeter)

def tri_check(s1, s2, s3):
  if s1 > s2 + s3:
    rez = False
  else:
    rez = True
  return rez

# Задані сторони трикутника
a = float(input("Введіть сторону a: "))
b = float(input("Введіть сторону b: "))
c = float(input("Введіть сторону c: "))
rez1 = tri_check(a, b, c)
rez2 = tri_check(b, a, c)
rez3 = tri_check(c, a, b)

print(True) if rez1==rez2==rez3 else print(False)