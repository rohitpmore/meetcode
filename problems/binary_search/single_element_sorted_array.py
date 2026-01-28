"""
Problem: Single Element in a Sorted Array
Difficulty: Medium
Time Limit: 30 min

Description:
You are given a sorted array of integers, nums, where all integers appear
twice except for one. Your task is to find and return the single integer
that appears only once.

The solution should have a time complexity of O(log n) or better and a
space complexity of O(1).

Constraints:
- 1 <= nums.length <= 10^3
- 0 <= nums[i] <= 10^3
- All integers appear exactly twice, except for one which appears once

Examples:

Example 1:
Input: nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
Output: 2

Example 2:
Input: nums = [3, 3, 7, 7, 10, 11, 11]
Output: 10

Example 3:
Input: nums = [1, 1, 2, 2, 3]
Output: 3

Example 4:
Input: nums = [1, 2, 2, 3, 3]
Output: 1
"""

from typing import List

"""
nums = 1 1 2 2 3 3 4 4 5 5 6 6 7 8 8 9 9

start = 9
end = 16
mid = 12
"""

def solution(nums: List[int]) -> int:

    if len(nums) == 1:
        return nums[0]
    
    start, end = 0, len(nums)-1

    while start <= end:
        mid = (start + end) // 2
        if mid > 0 and nums[mid] == nums[mid-1]:
            if (mid-1) % 2 == 0: #no disruption yet
                start = mid + 1
            else:
                end = mid - 1        
        elif mid + 1 < len(nums) and nums[mid] == nums[mid+1]:
            if mid % 2 == 0: #no disruption yet
                start = mid + 1
            else:
                end = mid - 1        
        else:
            return nums[mid]


TEST_CASES = [
    # (input_args, expected_output)
    (([1, 1, 2, 3, 3, 4, 4, 8, 8],), 2),
    (([3, 3, 7, 7, 10, 11, 11],), 10),
    (([1, 1, 2, 2, 3],), 3),
    (([1, 2, 2, 3, 3],), 1),
    (([1],), 1),
    (([1, 1, 2],), 2),
    (([1, 2, 2],), 1),
    (([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6],), 6),
    (([0, 0, 1, 1, 2, 2, 3, 3, 4, 5, 5],), 4),
    (([1, 1, 3, 5, 5],), 3),
]
