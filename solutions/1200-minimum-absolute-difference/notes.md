# 1200 - Minimum Absolute Difference

## Idea
The minimum absolute difference must occur between adjacent elements after sorting.

## Steps
1. Sort array
2. Compute differences between neighbors
3. Track smallest difference
4. Collect all pairs that match it

## Complexity
- Time: O(n log n) (sorting)
- Space: O(1) extra (excluding output)