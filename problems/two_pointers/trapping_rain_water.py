"""
Problem: Trapping Rain Water
Difficulty: Hard
Source: LeetCode #42 (Meta Top Interview Question)

Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The elevation map (shown as bars) can trap 6 units of rain water.

Visual:
       #
   #~~~##~#
 _#~##~####
 0102101321

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
- n == height.length
- 1 <= n <= 2 * 10^4
- 0 <= height[i] <= 10^5

Hints:
- At each position, water level = min(max_left, max_right) - height[i]
- Can precompute max_left and max_right arrays (O(n) space)
- Or use two pointers for O(1) space solution
"""

from typing import List


def solution(height: List[int]) -> int:
    # TODO(human): Implement your solution
    pass


TEST_CASES = [
    (([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],), 6),
    (([4, 2, 0, 3, 2, 5],), 9),
    (([1, 2, 3, 4, 5],), 0),
    (([5, 4, 3, 2, 1],), 0),
    (([3, 0, 0, 2, 0, 4],), 10),
    (([2, 0, 2],), 2),
]
