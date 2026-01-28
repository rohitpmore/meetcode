"""
Problem: Missing Number
Difficulty: Easy
Time Limit: 15 min

Description:
Given an array, nums, containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.

Constraints:
- n = nums.length
- 1 <= n <= 10^3
- 0 <= nums[i] <= n
- There are no duplicates in the array.

Example 1:
Input: nums = [3, 0, 1]
Output: 2
Explanation: n = 3, so range is [0,1,2,3]. 2 is missing.

Example 2:
Input: nums = [0, 1]
Output: 2
Explanation: n = 2, so range is [0,1,2]. 2 is missing.

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9, so range is [0..9]. 8 is missing.
"""

"""
nums = 0 1 3
i = 2

"""
def find_missing_number(nums):
    # time = O(n)
    # space = O(1)

    i = 0

    while i < len(nums):
        if i != nums[i] and nums[i] < len(nums):
            t = nums[i]
            nums[i], nums[t] = nums[t], nums[i]
        else:
            i += 1

    i = 0 

    for i in range(len(nums)):
        if i != nums[i]:
            return i
    return len(nums)



TEST_CASES = [
    # (input, expected_output)
    (([3, 0, 1],), 2),
    (([0, 1],), 2),
    (([9, 6, 4, 2, 3, 5, 7, 0, 1],), 8),
    (([0],), 1),
    (([1],), 0),
    (([1, 2],), 0),
    (([0, 2],), 1),
    (([0, 1, 2, 3, 4, 5, 6, 7, 9],), 8),
]

# For runner.py compatibility
solution = find_missing_number
