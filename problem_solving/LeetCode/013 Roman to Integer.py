class Solution:

    def romanToInt(self, roman_numeral):
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        prev_value = 0
        for symbol in reversed(roman_numeral):
            value = roman_numerals[symbol]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        return total


# Отримуємо введення користувача
roman_numeral = input("Введіть римське число: ").upper()

# Друкуємо отримане арабське число
print(Solution().romanToInt(roman_numeral))


#більш оптимізований код
class Solution2:
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    def romanToInt(self, roman_numeral: str) -> int:
        total = prev_value = 0
        for symbol in reversed(roman_numeral):
            value = self.roman_numerals[symbol]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        return total

# Отримуємо введення користувача
roman_numeral = input("Введіть римське число: ").upper()

# Друкуємо отримане арабське число
print(Solution2().romanToInt(roman_numeral))
