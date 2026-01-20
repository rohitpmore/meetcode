"""
Problem: Find the Duplicate Number
Difficulty: Medium

Given an array of positive numbers, nums, such that the values lie in the range
[1, n], inclusive, and that there are n+1 numbers in the array, find and return
the duplicate number present in nums.

There is only one repeated number in nums, but it may appear more than once.

Constraints:
- 1 <= n <= 10^3
- nums.length = n + 1
- 1 <= nums[i] <= n
- All integers in nums are unique, except for one integer that appears more than once
- You CANNOT modify the given array
- You must use only O(1) constant extra space

Example 1:
Input: nums = [1, 3, 4, 2, 2]
Output: 2

Example 2:
Input: nums = [3, 1, 3, 4, 2]
Output: 3

Example 3:
Input: nums = [1, 1]
Output: 1
"""

def solution(nums):
    # TODO(human): Implement your solution
    # Remember: O(1) space, cannot modify the array
    slow, fast = 0,0
    
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break

    fast = 0
    while True:
        slow = nums[slow]
        fast = nums[fast]

        if slow == fast:
            return fast


TEST_CASES = [
    (([1, 3, 4, 2, 2],), 2),
    #slow -> 0 -> 1 -> 3 -> 2 -> 4 -> 2 -> 4 -> 2 -> 4
    #fast -> 0 -> 3 -> 4 -> 4 -> 4 -> 4 -> 
    #cycle -> 0 
    (([3, 4, 4, 4, 2],), 4),
    #slow -> 0 -> 3 -> 4 -> 2 -> 4 -> 2
    #fast -> 0 -> 4 -> 4 -> 4 -> 
    (([3, 1, 3, 4, 2],), 3),
    (([1, 1],), 1),
    (([2, 2, 2, 2, 2],), 2),  # duplicate appears multiple times
    (([1, 4, 4, 2, 4],), 4),  # duplicate appears 3 times
    (([5, 1, 2, 3, 4, 5],), 5),  # duplicate at boundaries
]
