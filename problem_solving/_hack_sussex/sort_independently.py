def Solution(nums: list[int]) -> list[int]:
  even = sorted([x for i, x in enumerate(nums) if i % 2 == 0])
  odd = sorted([x for i, x in enumerate(nums) if i % 2 == 1], reverse=True)
  # print(even, odd) debug
  res = []
  while len(even) > 0 or len(odd) > 0:
    if len(even) > 0:
      res.append(even.pop(0))
    if len(odd) > 0:
      res.append(odd.pop(0))
  return res


nums = [4, 1, 2, 3]
print(Solution(nums))
