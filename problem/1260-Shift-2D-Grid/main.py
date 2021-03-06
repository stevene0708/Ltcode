"""
    Author: Weng Xiang Heng
    Date:2022/04/11
"""
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        list_=[]
        ans = []
        for row in grid:
            for column in row:
                list_.append(column)
                ans.append(0)
        
        for num in range(len(list_)):
            ans[(num+k)%len(list_)] = list_[num]
        
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                grid[row][column] = ans[row*len(grid[row])+column]
        return grid