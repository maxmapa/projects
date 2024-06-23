class Solution1:  #Brute Force

    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []  # No solution found


nums = [2, 7, 11, 15]
target = 9
print(Solution1().twoSum(nums, target))


class Solution2:  #Two-pass Hash Table

    def twoSum(self, nums, target):
        numMap = {}
        n = len(nums)

        # Build the hash table
        for i in range(n):
            numMap[nums[i]] = i

        # Find the complement
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]

        return []  # No solution found


nums = [2, 7, 11, 15]
target = 9
print(Solution2().twoSum(nums, target))


class Solution3:  #One-pass Hash Table

    def twoSum(self, nums, target):
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

        return []  # No solution found


nums = [2, 7, 11, 15]
target = 9
print(Solution3().twoSum(nums, target))

class Solution4: #One-pass Hash Table + enumerate
    def twoSum(self, nums: List[int], target: int) -> List[int]:#Аннотації зрозумілі Python 3.6+
        numMap = {}  # Ініціалізуємо хеш-таблицю
        for i, num in enumerate(nums):
            complement = target - num
            if complement in numMap:
                return [numMap[complement], i]  # Знайдено відповідні індекси, повертаємо результат
            numMap[num] = i  # Додаємо елемент у хеш-таблицю
        return []

nums = [2, 7, 11, 15]
target = 9
print(Solution4().twoSum(nums, target))