class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        used: set[int] = set()
        for n in nums:
            if n in used:
                return True
            used.add(n)
        return False
