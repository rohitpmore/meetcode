"""
Problem: Subsets (Bit Manipulation Approach)
Difficulty: Medium
Time Limit: 30 min

Given an array of integers, nums, find all possible subsets of nums, including the empty set.
This version uses bit manipulation instead of recursion.

Constraints:
- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10
- All the numbers of nums are unique.

Example 1:
Input: nums = [1, 2, 3]
Output: [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
"""

"""
Bit manipulation approach:

For n=3, iterate mask from 0 to 7 (2^3 - 1):

mask=0 (000): check each bit → []
mask=1 (001): bit 0 set    → [nums[0]] = [1]
mask=2 (010): bit 1 set    → [nums[1]] = [2]
mask=3 (011): bits 0,1 set → [nums[0], nums[1]] = [1,2]
mask=4 (100): bit 2 set    → [nums[2]] = [3]
mask=5 (101): bits 0,2 set → [nums[0], nums[2]] = [1,3]
mask=6 (110): bits 1,2 set → [nums[1], nums[2]] = [2,3]
mask=7 (111): all bits set → [nums[0], nums[1], nums[2]] = [1,2,3]

Key operations:
- Total masks: 1 << n  (equals 2^n)
- Check if bit i is set: mask & (1 << i)
"""

def solution(nums: list[int]) -> list[list[int]]:
    # time = O(n × 2^n)
    # space = O(n × 2^n) for result, O(n) auxiliary
    result = []
    n = len(nums)

    for mask in range(1<<n):
        subset = []

        for i in range(n):
            if mask & (1 << i):
                subset += [nums[i]]
        result.append(subset) 

    return result


# Test cases - order doesn't matter, so we compare as sets of tuples
TEST_CASES = [
    (([1, 2, 3],), [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]),
    (([0],), [[], [0]]),
    (([1, 2],), [[], [1], [2], [1, 2]]),
    (([-1, 0, 1],), [[], [-1], [0], [1], [-1, 0], [-1, 1], [0, 1], [-1, 0, 1]]),
]


def compare_results(result, expected):
    """Custom comparator since order doesn't matter"""
    if result is None:
        return False
    result_set = {tuple(sorted(x)) for x in result}
    expected_set = {tuple(sorted(x)) for x in expected}
    return result_set == expected_set
