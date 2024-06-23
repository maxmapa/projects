# Runtime 47ms Beats 5.42% Memory 16.38MB Beats 99.89%
class Solution1: # просте рішення, саме так ми б робили у Ms Word

  def isValid(self, s: str) -> bool:
    while '()' in s or '[]' in s or '{}' in s:
      s = s.replace('()', '').replace('[]', '').replace('{}', '')
    return False if len(s) != 0 else True

s = input("Введіть рядок: ")#string s containing just the characters '(', ')', '{', '}', '[' and ']'
print(Solution1().isValid(s))

# Runtime 34ms Beats 67.27%
class Solution2:
  def isValid(self, s: str) -> bool:
      stack = []
      mapping = {")":"(", "}":"{", "]":"["}

      for char in s:
          if char in mapping.values():
              stack.append(char)
          elif char in mapping.keys():
              if not stack or mapping[char] != stack.pop():
                  return False

      return not stack

s = input("Введіть рядок: ")#string s containing just the characters '(', ')', '{', '}', '[' and ']'
print(Solution2().isValid(s))

class Solution3():# best Runtime and memory
    def isValid(self, s):
        stack = [] # only use append and pop
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for bracket in s:
            if bracket in pairs:
                stack.append(bracket)
            elif len(stack) == 0 or bracket != pairs[stack.pop()]:
                return False

        return len(stack) == 0

s = input("Введіть рядок: ")#string s containing just the characters '(', ')', '{', '}', '[' and ']'
print(Solution3().isValid(s))
