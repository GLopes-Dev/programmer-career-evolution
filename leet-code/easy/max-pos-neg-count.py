class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        first_non_negative = len(nums)
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] >= 0:
                first_non_negative = middle
                right = middle - 1
            else:
                left = middle + 1
        neg = first_non_negative

        left, right = 0, len(nums) - 1
        first_pos = len(nums)
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] > 0:
                first_pos = middle
                right = middle - 1
            else:
                left = middle + 1
        pos = len(nums) - first_pos

        return max(neg, pos)