values = []
for x in range(10):
  values.append(x)
print(values)
#comprehension
val = [i for i in range(10)]
print(val)


#Get all even numbers 0-20
evens = []
for number in range(20):
  is_even = number % 2 == 0
  if is_even:
    evens.append(number)
print(evens)
#comprehension
even = [number for number in range(20) if number % 2 == 0]
print(even)
#or
ev = [number for number in range(0,20,2)]
print(ev)


#nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = []
for row in matrix:
  for number in row:
    flattened.append(number)
print(flattened)
#comprehension
flattened = [num for row in matrix for num in row]
print(flattened)


#sum of squares
sum_of_squares = sum(x**2 for x in range(100))
"""if done with standard approach we will save all square values in memory and than sum them

with comprehension approach we use so called generator expression
generato in python only returns values when they needed"""