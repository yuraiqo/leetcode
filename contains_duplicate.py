class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        used = set()
        for num in nums:
            if num in used:
                return True
            used.add(num)
        return False
