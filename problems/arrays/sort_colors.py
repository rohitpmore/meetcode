"""
Problem: Sort Colors
Difficulty: Medium
Source: LeetCode #75 (Dutch National Flag Problem)

Given an array, colors, which contains a combination of the following three elements:
- 0 (Representing red)
- 1 (Representing white)
- 2 (Representing blue)

Sort the array in place so that the elements of the same color are adjacent,
and the final order is: red (0), then white (1), and then blue (2).

Note: You are not allowed to use any built-in sorting functions.
The goal is to solve this efficiently without extra space.

Example 1:
Input: colors = [2, 0, 2, 1, 1, 0]
Output: [0, 0, 1, 1, 2, 2]

Example 2:
Input: colors = [2, 0, 1]
Output: [0, 1, 2]

Example 3:
Input: colors = [0]
Output: [0]

Constraints:
- n = colors.length
- 1 <= n <= 300
- colors[i] is either 0, 1, or 2
"""

# colors -> 0, 2, 1
# low = 1, mid = 1, high = 2


def solution(colors: list[int]) -> list[int]:
    # TODO(human): Implement your solution (sort in-place)
    # Return the modified list

    low, mid, high = 0, 0, len(colors) - 1

    while mid <= high : 
        if colors[mid] == 0 : 
            colors[mid], colors[low] = colors[low], colors[mid]
            low += 1
            mid += 1
        elif colors[mid] == 2 :
            colors[mid], colors[high] = colors[high], colors[mid]
            high -=1
        else: 
            mid += 1
        
    return colors


TEST_CASES = [
    # Basic cases
    ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
    ([2, 0, 1], [0, 1, 2]),

    # Single element
    ([0], [0]),
    ([1], [1]),
    ([2], [2]),

    # Already sorted
    ([0, 0, 1, 1, 2, 2], [0, 0, 1, 1, 2, 2]),

    # Reverse sorted
    ([2, 2, 1, 1, 0, 0], [0, 0, 1, 1, 2, 2]),

    # All same color
    ([0, 0, 0], [0, 0, 0]),
    ([1, 1, 1], [1, 1, 1]),
    ([2, 2, 2], [2, 2, 2]),

    # Two colors only
    ([1, 0, 1, 0], [0, 0, 1, 1]),
    ([2, 0, 2, 0], [0, 0, 2, 2]),
    ([2, 1, 2, 1], [1, 1, 2, 2]),

    # Two elements
    ([1, 0], [0, 1]),
    ([2, 0], [0, 2]),

    # Longer mixed case
    ([0, 1, 2, 0, 1, 2, 0, 1, 2], [0, 0, 0, 1, 1, 1, 2, 2, 2]),

    # Edge: all at boundaries
    ([2, 2, 2, 0, 0, 0], [0, 0, 0, 2, 2, 2]),
]
