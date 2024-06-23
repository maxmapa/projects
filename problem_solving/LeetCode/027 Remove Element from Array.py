class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
      i = 0
      for x in nums:
          if x != val:
              nums[i] = x
              i += 1
      return i

nums = [0,1,2,2,3,0,4,2]
val = 2
print(Solution().removeElement(nums, val))

class Solution2: # less effective
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0

        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1

        return(len(nums))
