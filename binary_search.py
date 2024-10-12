class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums)
        while low < high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                high = mid
            else:
                low = mid + 1
        return -1
