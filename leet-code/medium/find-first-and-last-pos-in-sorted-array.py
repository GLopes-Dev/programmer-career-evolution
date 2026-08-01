#1 Try - TLE
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        pos = []
        if target not in nums:
            pos = [-1, -1]
            return pos
        left, right, answer = 0, len(nums) - 1, 0
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                answer = middle
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        pos.append(answer)
        left, right, answer = 0, len(nums) - 1, 0
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                answer = middle
                left = middle + 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        pos.append(answer)
        return pos

#2 Try - 83/83 Testcases Passed
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        pos = []
        left, right, answer = 0, len(nums) - 1, 0
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                answer = middle
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        pos.append(answer)
        left, right, answer = 0, len(nums) - 1, 0
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                answer = middle
                left = middle + 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        pos.append(answer)
        if answer == 0:
            pos = [-1, -1]
        return pos

#3 Try - 88/88 Testcases passed - O(log n) Time complexity achieved
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        pos = []
        left, right, answer = 0, len(nums) - 1, -1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                answer = middle
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        pos.append(answer)
        left, right, answer = 0, len(nums) - 1, -1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                answer = middle
                left = middle + 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        pos.append(answer)
        if answer == -1:
            pos = [-1, -1]
        return pos
    