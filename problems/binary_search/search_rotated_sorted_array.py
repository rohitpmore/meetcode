"""
Problem: Search in Rotated Sorted Array
Difficulty: Medium
Time Limit: 30 min

Description:
You are given a sorted integer array, nums, and an integer, target.
The array may have been rotated by an arbitrary number of positions.
Your task is to find and return the index of target in this array.
If target does not exist, return -1.

Example of rotation:
Original sorted array: [1, 10, 20, 47, 59, 63, 75, 88, 99, 107, 120, 133, 155, 162, 176, 188, 199, 200, 210, 222]
After rotating 6 times: [176, 188, 199, 200, 210, 222, 1, 10, 20, 47, 59, 63, 75, 88, 99, 107, 120, 133, 155, 162]

Constraints:
- All values in nums are unique
- The values in nums are sorted in ascending order (before rotation)
- The array may have been rotated by some arbitrary number (including 0)
- 1 <= nums.length <= 1000
- -10^4 <= nums[i] <= 10^4
- -10^4 <= target <= 10^4

Examples:

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 1
Output: 0

Example 4:
Input: nums = [3,1], target = 1
Output: 1
"""

from typing import List


def solution(nums: List[int], target: int) -> int:

    start, end = 0, len(nums)-1

    while start <= end:
        mid = (start + end) // 2

        if target == nums[mid]:
            return mid

        if nums[start] <= nums[mid]:
            if target >= nums[start] and target <= nums[mid]:
                end = mid -1
            else:
                start = mid + 1
        else:
            if target >= nums[mid] and target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1

    return -1


TEST_CASES = [
    # (input_args, expected_output)
    (([4, 5, 6, 7, 0, 1, 2], 0), 4),
    (([4, 5, 6, 7, 0, 1, 2], 3), -1),
    (([1], 1), 0),
    (([3, 1], 1), 1),
    (([5, 1, 3], 5), 0),
    (([4, 5, 6, 7, 8, 1, 2, 3], 8), 4),
    (([2, 3, 4, 5, 6, 7, 8, 9, 1], 9), 7),
    (([3, 4, 5, 1, 2], 1), 3),
    (([11, 13, 15, 17], 13), 1),  # No rotation case
    (([2, 1], 2), 0),
]
