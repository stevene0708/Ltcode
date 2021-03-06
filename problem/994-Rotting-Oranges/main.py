"""
    Author: Weng Xiang Heng
    Date:2021/10/29
"""
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rounds = 0
        queue = []
        queue_ = []
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if(grid[i][j] == 2):
                    queue.append((i, j))
                    
        while(queue):
            m, n = queue.pop(0)

            if(m-1 <= len(grid)-1 and m-1 >= 0):
                if(grid[m-1][n] == 1):
                    grid[m-1][n] = 2
                    queue_.append((m-1, n))
            if(m+1 <= len(grid)-1 and m+1 >= 0):
                if(grid[m+1][n] == 1):
                    grid[m+1][n] = 2
                    queue_.append((m+1, n))
            if(n-1 <= len(grid[m])-1 and n-1 >= 0):
                if(grid[m][n-1] == 1):
                    grid[m][n-1] = 2
                    queue_.append((m, n-1))
            if(n+1 <= len(grid[m])-1 and n+1 >= 0):
                if(grid[m][n+1] == 1):
                    grid[m][n+1] = 2
                    queue_.append((m, n+1))
            if(not queue and queue_):
                queue = queue_
                queue_ = []
                rounds += 1
                
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if(grid[i][j] == 1):
                    rounds = -1
                    
        return rounds
            