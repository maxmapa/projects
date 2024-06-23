n = int(input("Введіть початкове значення: "))
s="#"

while n >= 1:
    print(n, s*n)
    n = n - 1

# acording to the scheme
n = int(input("Введіть початкове значення: "))
s="#"
count = n

while count>0:
  print(count, "", end="")
  count=count-1
  count1=0
  while count1<count+1:
    print(s, end="")
    count1+=1
  print() 