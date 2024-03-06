class Solution:
    """ this is the problem: https://leetcode.com/problems/island-perimeter/ """
    def islandPerimeter(self, grid: list[list[int]]) -> int:

        # starting from row 0 and col 0
        row = 0
        col = 0

        val = 0 # final value
        for rows in grid:
            # for each row, need to add the ones
            
            for cell in rows:
                if cell == 1:
                    val += 4
                    # if it is 1, then look up and left
                    prev_row = row - 1
                    prev_col = col - 1
                    if prev_row >= 0: # can check upper
                        if grid[prev_row][col] == 1:
                            val -= 2
                    if prev_col >= 0: # can check left
                        if grid[row][prev_col] == 1:
                            val -= 2

                else:
                    pass
                col += 1

            row += 1
            col = 0

        return val
    
s = Solution()

grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
ret = s.islandPerimeter(grid)
print(f'ret is: {ret}')   