class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        need = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in need:
                return [need[diff], i]
            need[num] = i
