def count_subtraction_cycles(nums: list[int]) -> int:
  nums = set(nums)
  nums.discard(0)
  return len(nums)

nums = [1,5,0,3,5]
print(count_subtraction_cycles(nums))


#solution 2
def count_subtraction_cycles(nums):
  cycles = 0

  while any(num > 0 for num in nums):
      # Сортуємо список
      nums.sort()

      # Знаходимо найменше ненульове число
      min_positive = next(num for num in nums if num > 0)

      # Віднімаємо це число від усіх ненульових елементів
      nums = [num - min_positive if num > 0 else num for num in nums]

      # Збільшуємо кількість циклів
      cycles += 1

  return cycles

# Приклад використання:
nums = [1, 5, 0, 3, 5]
print(count_subtraction_cycles(nums))  # Виведе: 3
