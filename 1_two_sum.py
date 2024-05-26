class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prev: dict[int, int] = {}
        for i, n in enumerate(nums):
            x = target - n
            if x in prev:
                return [prev[x], i]
            prev[n] = i
