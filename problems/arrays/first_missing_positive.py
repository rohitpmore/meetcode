"""
Problem: First Missing Positive
Difficulty: Hard
Time Limit: 40 min

Description:
Given an unsorted integer array, nums, return the smallest missing positive integer.
Create an algorithm that runs with O(n) time complexity and utilizes a constant
amount of space.

Note: The smallest missing positive isn't the first positive number that's missing
in the range of elements in the input, but the first positive number that's missing
if we start from 1.

Constraints:
- 1 <= nums.length <= 10^5
- -2^31 <= nums[i] <= 2^31 - 1

Example 1:
Input: nums = [1, 2, 0]
Output: 3
Explanation: 1 and 2 are present, so smallest missing positive is 3

Example 2:
Input: nums = [3, 4, -1, 1]
Output: 2
Explanation: 1 is present, 2 is missing

Example 3:
Input: nums = [7, 8, 9, 11, 12]
Output: 1
Explanation: No positive numbers starting from 1, so answer is 1
"""
"""
nums = 1 -1 3 4

i = 3

"""

def first_missing_positive(nums):

    # time = O(n)
    # space = O(1)

    i = 0 
    while i < len(nums):
        if i + 1 != nums[i] and nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[nums[i]-1]:
            t = nums[i] - 1
            nums[i], nums[t] = nums[t], nums[i]
        else:
            i += 1
    
    i = 0
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return i + 1
    return len(nums)+1


TEST_CASES = [
    # (input, expected_output)
    (([1, 2, 0],), 3),
    (([3, 4, -1, 1],), 2),
    (([7, 8, 9, 11, 12],), 1),
    (([1],), 2),
    (([2],), 1),
    (([1, 2, 3],), 4),
    (([-1, -2, -3],), 1),
    (([1, 1, 1, 1],), 2),
]

# For runner.py compatibility
solution = first_missing_positive
