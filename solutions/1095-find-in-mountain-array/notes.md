# 1095 - Find in Mountain Array

## Problem
Mountain array increases strictly to a peak, then decreases strictly.
Need index of target with minimal calls.

## Strategy (3 binary searches)
1) Find peak index:
   - compare mid and mid+1 to decide slope

2) Binary search left side (ascending)

3) Binary search right side (descending)

Return first found (left checked first, so smallest index).

## Complexity
Time: O(log n)
Calls: O(log n) gets per search (constant factor)
Space: O(1)

The question mentioned that you cannot access the mountain array directly. You may only access the array using a MountainArray interface: MountainArray.get(k) returns the element of the array at index k (0-indexed).
We can’t use normal array access because the problem only exposes the data through an interface, which simulates restricted or remote access and forces us to use an efficient, logarithmic solution.”

“I cache results of MountainArray.get(i) so repeated index accesses don’t consume extra API calls, which keeps me under the 100-call limit.”

Why this keeps calls under 100
Binary search touches about log₂(n) positions.
Even if:
•	peak search ≈ log n
•	left search ≈ log n
•	right search ≈ log n
Total distinct indices accessed ≈ 3 log₂(n)
For n = 10^5:
log₂(n) ≈ 17
Total ≈ 51 get() calls
Safely under 100.
Since get() calls are limited, you should memoize:
•	cache[i] = mountainArr.get(i) the first time you request it
•	subsequent accesses reuse the cached value with 0 additional get calls

Because the array is mountain-shaped, I first locate the peak using binary search by comparing get(mid) and get(mid+1). Then I binary search the increasing part [0..peak]. If not found, I binary search the decreasing part [peak+1..n-1] with inverted comparisons. 

