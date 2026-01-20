"""
Problem: Minimum Size Subarray Sum
Difficulty: Medium
Time Limit: 30 min

Description:
Given an array of positive integers, nums, and a positive integer, target,
find the minimum length of a contiguous subarray whose sum is greater than
or equal to the target. If no such subarray is found, return 0.

Constraints:
- 1 <= target <= 10^4
- 1 <= nums.length <= 10^3
- 1 <= nums[i] <= 10^3

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1
Explanation: The subarray [4] has sum >= 4 with minimal length.

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
Explanation: No subarray sums to 11 or more.
"""


"""
    arr -> 2 3 1 2 4 3
    target -> 7
    L -> 6
    ws -> 5
    we -> 6
    rs -> 3
    minLen -> 2

"""
def solution(target: int, nums: list[int]) -> int:

    ws = 0
    we = 0
    L = len(nums)
    rs = 0
    minLen = float('inf')

    for we in range(L):
        rs += nums[we]

        while rs >= target and ws < L:
            minLen = min(minLen, we - ws + 1)
            rs -= nums[ws]
            ws += 1
    
    if minLen == float('inf'):
        return 0
    else:
        return minLen
        
    



TEST_CASES = [
    ((7, [2, 3, 1, 2, 4, 3]), 2),
    ((4, [1, 4, 4]), 1),
    ((11, [1, 1, 1, 1, 1, 1, 1, 1]), 0),
    ((15, [1, 2, 3, 4, 5]), 5),
    ((5, [2, 3, 1, 1, 1, 1, 1]), 2),
    ((100, [1, 2, 3, 4, 5]), 0),
    ((3, [1, 1, 1, 1, 1, 1, 1]), 3),
]
