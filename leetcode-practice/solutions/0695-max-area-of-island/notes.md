# 695 - Max Area of Island

## Idea
Scan the grid. When we find a `1`, we run a flood-fill (DFS/BFS) to count the entire connected component (4-directionally connected land). Track the largest area across all islands.

## Approach
- Iterate all cells
- If `grid[r][c] == 1`, start DFS
- DFS counts cells in this island and marks them visited by setting them to `0`
- Keep a running maximum

## Why it works
Each land cell is counted exactly once:
- When we visit a cell, we immediately mark it visited (set to 0)
- So it can’t be counted again in another DFS
Thus every island’s area is computed correctly, and we return the maximum.

## Complexity
Let `m = rows`, `n = cols`:
- Time: O(m*n) because each cell is visited at most once
- Space: O(m*n) worst case for the DFS stack (all land)

## Edge cases
- Empty grid -> 0
- All zeros -> 0
- Single cell (1) -> 1
- Large islands: iterative DFS avoids recursion depth issues in Python