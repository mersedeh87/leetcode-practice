## Step 1 — Understand the problem
"""You’re given a grid of `0`s and `1`s:
- `1` = land
- `0` = water
An “island” is land connected **4-directionally** (up/down/left/right).
The “area” is **how many `1` cells** are in that island.

Goal: return the **maximum** island area. If no land exists, return `0`.

---"""

## Step 2 — Key idea
"""This is a classic **connected components in a grid** problem.

Approach:
- Scan every cell in the grid
- When you find a `1`, that starts a new island
- Run **DFS or BFS** from that cell to count all connected land cells
- Mark visited cells so you don’t count them again
- Track the maximum area found"""
from typing import List, Tuple
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m , n = len(grid), len(grid[0])
        best = 0 
        def dfs (i,j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j] != 1:
                return 0
            grid[i][j] = 0
            return ( 1+ dfs (i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1))

        for i in range (m):
            for j in range (n):
                if grid[i][j] == 1:
                    
                    area = dfs(i,j)
                    best = max(best,area)
        return best 
if __name__ == "__main__":
    # Basic quick tests (you can expand these over time)
    s = Solution()

    grid1 = [
        [0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 1, 0, 0],
        [1, 1, 0, 0, 0],
    ]
    # max island area here is 5 (the plus-shape)
    print(s.maxAreaOfIsland([row[:] for row in grid1]))  # expected: 5

    