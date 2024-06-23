#simple
#Input
mas = []
n = int(input("Введіть число: "))
#Code
while n!=0:
  mas.append(n%10)
  n=n//10
count=len(mas)//2  
flag = True

for i in range(count+1):
  if mas[i] != mas[len(mas)-1-i]:
    flag = False
    break      
#Output
if flag:
  print("Palindrome")
else:
  print("Not palindrome")

class Solution2:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        reversed_num = 0

        while x > reversed_num:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10

        return x == reversed_num or x == reversed_num // 10
print(Solution2().isPalindrome(12346321))
#Best practice
import math

class Solution3:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        num_digits = 1 + math.floor(math.log10(x))
        fst = 10 ** (num_digits - 1)

        while x > 0:
            last = x % 10
            if last != x // fst:
                return False
            x = (x % fst) // 10
            fst //= 100  # Зменшуємо fst на 2 розряди, оскільки відкидаємо по одній цифрі з початку та кінця числа
            print(x)
            print(fst)
        return True
print(Solution3().isPalindrome(12346321))