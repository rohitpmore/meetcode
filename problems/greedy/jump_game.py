"""
Problem: Jump Game I
Difficulty: Medium
Time Limit: 30 min

You are given an integer array nums, where each element represents the maximum
number of steps you can move forward from that position.

You always start at index 0 (the first element), and at each step, you may jump
to any of the next positions within the range allowed by the current element's value.

Return TRUE if you can reach the last index, or FALSE otherwise.

Constraints:
- 1 <= nums.length <= 10^3
- 0 <= nums[i] <= 10^3

Example 1:
Input: nums = [2, 3, 1, 1, 4]
Output: True
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3, 2, 1, 0, 4]
Output: False
Explanation: You will always arrive at index 3 no matter what. Its maximum jump
length is 0, which makes it impossible to reach the last index.

Example 3:
Input: nums = [0]
Output: True
Explanation: Already at the last index.
"""

"""
nums = 1 0 1 0

current_level_end = 1
farthest = 1
i = 1
"""

def solution(nums: list[int]) -> bool:
    if len(nums) <= 1:
        return True
    
    current_level_end = 0
    farthest = 0 

    for i in range(0, len(nums)-1):
        farthest = max(farthest, i + nums[i])
        if i == current_level_end:
            if current_level_end == farthest:
                return False
            current_level_end = farthest

    if farthest >= len(nums) -1 :
        return True
    else:
        return False



# Test cases
TEST_CASES = [
    (([2, 3, 1, 1, 4],), True),
    (([3, 2, 1, 0, 4],), False),
    (([0],), True),
    (([1, 2, 3],), True),
    (([1, 0, 1, 0],), False),
    (([2, 0, 0],), True),
    (([1, 1, 1, 0],), True),
    (([5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0],), True),
]
