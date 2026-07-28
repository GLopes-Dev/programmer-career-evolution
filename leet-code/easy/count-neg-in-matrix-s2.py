# O(m + n) solution (Staircase) Left-Inf

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        lines, columns = len(grid), len(grid[0])
        l = lines - 1
        c = 0
        neg = 0
        while l >= 0 and c < columns:
            if grid[l][c] < 0:
                neg += columns - c
                l -= 1
            else:
                c += 1
            
        return neg