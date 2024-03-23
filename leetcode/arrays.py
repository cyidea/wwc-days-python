class Solution:
    
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        """ this is the problem: https://leetcode.com/problems/island-perimeter/ """
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
    
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """ https://leetcode.com/problems/3sum/ """
        
        # create a dictionary with indexes as values
        dic = self.create_dictionary(nums)
        #print(dic)

        # here is a set that contains 

        # loop through the nums
        index1 = 0
        index2 = 0
        retval = []
        already_checked = []
        all_zero_added = False
        for val in nums:
            index2 = index1 + 1
            for val2 in nums[index1 + 1:]:
                    # print(f'index2 is: {index2}')
                    val_need = 0 - val - val2

                    # print(f'{val} and {val2} so need this val: {val_need}')
                    if val_need in dic:

                        # check to make sure (val, val2, val_need) is not already in retval
                        # otherwise just continue to the next
                        if self.exists_already(val, val2, retval, already_checked, all_zero_added):
                            index2 += 1
                            continue

                        vals = dic[val_need]
                        # print(f'found {val_need} in dic {vals}')
                        # find the index that is not index1 or index2
                        for index_val in vals:
                            if index1 != index_val and index2 != index_val:
                                if val == 0 and val2 == 0 and val_need == 0:
                                    all_zero_added = True
                                tup = [val, val2, val_need]
                                # print(f'appending tup: {tup}')
                                retval.append(tup)
                                break
                    index2 += 1
            index1 += 1

        # print(f'retval is: {retval}')

        return retval

    def exists_already(self, val, val2, retval, already_checked, all_zero_added):
        # print('\n')
        # print(f'val: {val} and val2: {val2}')
        # print(f'retval are: {retval}')
        if val == 0 and val2 == 0 and all_zero_added:
            return True
        
        for vals in already_checked:
            if (val in vals) and (val2 in vals):
                if (val == 0) and (val2 == 0):
                    # if there are already 2 zeros then it is all set
                    if vals.count(0) >= 2:
                        return True
                else:
                    return True

        for vals in retval:
            if (val in vals) and (val2 in vals):
                
                if (val == 0) and (val2 == 0):
                    # if there are already 2 zeros then it is all set
                    if vals.count(0) >= 2:
                        already_checked.append([val, val2])
                        return True
                else:
                    already_checked.append([val, val2])
                    return True
        return False

    def create_dictionary(self, nums):
        dic = {}
        index = 0
        for val in nums:
            if val in dic:
                vals = dic[val]
                vals.append(index)
            else:
                vals = [index]
                dic[val] = vals
            index += 1

        return dic
    
s = Solution()

# grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# ret = s.islandPerimeter(grid)
# print(f'ret is: {ret}')   

# grid = [-1,0,1,2,-1,-4]
#  grid = [1,2,-2,-1]
# grid = [0, 0, 0]
# grid = [0, 0, 0, 1, -1]
# not working grid = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]
grid = [-4, 4,-2,0,4,0,-2,3,1,-5,0]
ret = s.threeSum(grid)
print(f'ret is: {ret}')