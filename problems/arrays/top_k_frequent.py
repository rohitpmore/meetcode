"""
Problem: Top K Frequent Elements
Difficulty: Medium
Source: LeetCode #347 (Meta Interview Question)

Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- k is in the range [1, the number of unique elements in the array].
- It is guaranteed that the answer is unique.

Follow-up: Your algorithm's time complexity must be better than O(n log n),
where n is the array's size.

Hints:
- Can you use a hash map to count frequencies?
- Think about bucket sort or heap for getting top K
"""

from typing import List


def solution(nums: List[int], k: int) -> List[int]:
    # TODO(human): Implement your solution
    pass


# Note: Order doesn't matter in output
TEST_CASES = [
    (([1, 1, 1, 2, 2, 3], 2), [1, 2]),
    (([1], 1), [1]),
    (([1, 2], 2), [1, 2]),
    (([4, 4, 4, 4, 5, 5, 6], 1), [4]),
    (([1, 1, 2, 2, 3, 3, 4], 3), [1, 2, 3]),
]
