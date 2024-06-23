#best code
class Solution:

  def longestCommonPrefix(self, strs):
    ans = ""
    strs = sorted(strs)
    first = strs[0]
    last = strs[-1]
    for i in range(min(len(first), len(last))):
      if first[i] != last[i]:
        return ans
      ans += first[i]
    return ans


# Отримуємо введення користувача
strs = ["dfog", "dfear", "dfeed"]

# Друкуємо отримане арабське число
print(Solution().longestCommonPrefix(strs))


#my good code
class Solution2:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        prefix = ""
        min_length = min(len(word) for word in strs)

        for i in range(min_length):
            current_char = strs[0][i]

            if all(word[i] == current_char for word in strs):
                prefix += current_char
            else:
                break

        return prefix
strs = ["small","smash","smack"]

# Друкуємо отримане арабське число
print(Solution2().longestCommonPrefix(strs))