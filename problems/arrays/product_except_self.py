"""
Problem: Product of Array Except Self
Difficulty: Medium
Source: LeetCode #238 (Meta Top Interview Question)

Given an integer array nums, return an array answer such that answer[i] is equal
to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
- 2 <= nums.length <= 10^5
- -30 <= nums[i] <= 30
- The product of any prefix or suffix is guaranteed to fit in a 32-bit integer.

Follow-up: Can you solve the problem in O(1) extra space complexity?
(The output array does not count as extra space for space complexity analysis.)

Hints:
- Think about prefix and suffix products
- For each position, you need product of everything to the left * product of everything to the right
"""

from typing import List


def solution(nums: List[int]) -> List[int]:
    # TODO(human): Implement your solution
    pass


TEST_CASES = [
    (([1, 2, 3, 4],), [24, 12, 8, 6]),
    (([-1, 1, 0, -3, 3],), [0, 0, 9, 0, 0]),
    (([2, 3],), [3, 2]),
    (([1, 1, 1, 1],), [1, 1, 1, 1]),
    (([0, 0],), [0, 0]),
    (([2, 0, 3],), [0, 6, 0]),
]
