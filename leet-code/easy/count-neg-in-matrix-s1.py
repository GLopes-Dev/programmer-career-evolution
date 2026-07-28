# O(m log n) Solution

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        neg = 0
        for linha in grid:
            left = 0
            right = len(linha) - 1
            first_non_negative = len(linha)
            while left <= right:
                middle = (left + right) // 2
                if linha[middle] < 0:
                    first_non_negative = middle
                    right = middle - 1
                else:
                    left = middle + 1
            neg += len(linha) - first_non_negative
        
        return neg
