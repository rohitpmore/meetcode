"""
Problem: Container With Most Water
Difficulty: Medium
Source: LeetCode #11 (Meta Interview Question)

You are given an integer array height of length n. There are n vertical lines
drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the
container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The vertical lines are drawn at positions 0-8.
The max area is between lines at index 1 and 8: min(8,7) * (8-1) = 7 * 7 = 49

Example 2:
Input: height = [1,1]
Output: 1

Constraints:
- n == height.length
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4

Hints:
- Use two pointers at both ends
- The width decreases as pointers move inward, so you need taller lines
- Move the pointer with the shorter line (can't do better keeping short line)
"""

from typing import List


def solution(height: List[int]) -> int:
    # TODO(human): Implement your solution
    pass


TEST_CASES = [
    (([1, 8, 6, 2, 5, 4, 8, 3, 7],), 49),
    (([1, 1],), 1),
    (([4, 3, 2, 1, 4],), 16),
    (([1, 2, 1],), 2),
    (([2, 3, 4, 5, 18, 17, 6],), 17),
]
