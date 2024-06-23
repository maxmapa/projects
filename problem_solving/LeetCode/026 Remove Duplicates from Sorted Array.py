class Solution1:
  def removeDuplicates(self, nums: List[int]) -> int:

      i,j=0,1
      while i<=j and j<len(nums):
          if nums[i]==nums[j]:
              j+=1

          else:
              nums[i+1]=nums[j]
              i+=1

      return i+1

class Solution2:
  def removeDuplicates(self, nums: List[int]) -> int:
      if not nums:
          return 0

      next_unique = 1
      for i in range(1, len(nums)):
          if nums[i] != nums[next_unique - 1]:
              nums[next_unique] = nums[i]
              next_unique += 1

      return next_unique

class Solution3:
  def removeDuplicates(self, nums: List[int]) -> int:
      i = 0
      for j, num in enumerate(nums):
          if j == 0 or num != nums[j - 1]:
              nums[i] = num
              i += 1
      return i


