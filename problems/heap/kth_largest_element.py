"""
Problem: Kth Largest Element in an Array
Difficulty: Medium
Time Limit: 30 min

Description:
Given an integer array, nums, and an integer, k, determine and return the
kth largest element in the array.

Note: The kth largest element is defined with respect to the array's sorted
order (descending), and does not necessarily correspond to the kth unique value.

Example 1:
Input: nums = [3, 2, 1, 5, 6, 4], k = 2
Output: 5
Explanation: Sorted descending: [6, 5, 4, 3, 2, 1], 2nd largest is 5

Example 2:
Input: nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
Output: 4
Explanation: Sorted descending: [6, 5, 5, 4, 3, 3, 2, 2, 1], 4th largest is 4

Constraints:
- 1 <= k <= nums.length <= 10^3
- -10^4 <= nums[i] <= 10^4
"""

from typing import List

from heapq import heapify, heappush,heappushpop

"""
nums = 5,2,9,-3,7
k = 5th largest i.e. -3

mh = [5,2,9,-3,7]
i = 8

"""

def solution(nums: List[int], k: int) -> int:
    # TODO(human): Implement your solution
    # time -> O(n log k)
    # space -> O(log k) 
    mh = []
    heapify(mh)

    for i in range(k):
        heappush(mh, nums[i])

    i = k
    while i < len(nums):
        if nums[i] > mh[0]:
            _ = heappushpop(mh, nums[i])
        i += 1
    
    return mh[0]


TEST_CASES = [
    # (input_args, expected_output)
    (([3, 2, 1, 5, 6, 4], 2), 5),
    (([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4),
    (([1], 1), 1),
    (([7, 7, 7, 7], 2), 7),
    (([-1, -2, -3, -4], 1), -1),
    (([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5), 6),
]
