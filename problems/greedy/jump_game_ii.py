"""
Problem: Jump Game II
Difficulty: Medium
Time Limit: 30 min

In a single player jump game, the player starts at one end of a series of
squares and aims to reach the last square.

At each turn, the player can take up to s steps toward the last square,
where s is the value of the current square.

For example, if the value of the current square is 3, the player can take
either 3 steps, 2 steps, or 1 step in the direction of the last square.
The player cannot move in the opposite direction.

You've been provided with the nums integer array, representing the series
of squares. You're initially positioned at the first index of the array.

Find the minimum number of jumps needed to reach the last index of the array.

You may assume that you can always reach the last index.

Constraints:
- 1 <= nums.length <= 10^3
- 0 <= nums[i] <= 10^3

Example 1:
Input: nums = [2, 3, 1, 1, 4]
Output: 2
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [2, 3, 0, 1, 4]
Output: 2

Example 3:
Input: nums = [1]
Output: 0
Explanation: Already at the last index, no jumps needed.
"""

"""
nums = [[2, 3, 1, 1, 4]
N = 5


"""

def solution(nums: list[int]) -> int:
    if len(nums) <= 0:
        return 0
    
    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(0, len(nums)-1):
        farthest = max(farthest, i + nums[i])

        if i == current_end:
            jumps += 1
            current_end = farthest

            if current_end >= len(nums):
                break

    return jumps
    


# Test cases
TEST_CASES = [
    (([2, 3, 1, 1, 4],), 2),
    (([2, 3, 0, 1, 4],), 2),
    (([1],), 0),
    (([1, 2, 3],), 2),
    (([3, 2, 1],), 1),
    (([1, 1, 1, 1],), 3),
    (([5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0],), 3),
]
