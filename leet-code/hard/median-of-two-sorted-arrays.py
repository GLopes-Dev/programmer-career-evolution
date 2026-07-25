class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        median = 0
        m = len(nums)
        ini = 0
        fim = m - 1
        meio = (ini + fim) // 2
        if m % 2 == 0:
            median = (nums[meio] + nums[meio + 1]) / 2
        else:
            median = nums[meio]
        return median