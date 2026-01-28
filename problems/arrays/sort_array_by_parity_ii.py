"""
Problem: Sort Array By Parity II
Difficulty: Easy
Time Limit: 15 min

Description:
You are given an integer array nums, where exactly half of the elements are even,
and the other half are odd.

Rearrange nums such that:
- All even numbers are placed at even indexes [0, 2, 4, ...]
- All odd numbers are placed at odd indexes [1, 3, 5, ...]

You may return any valid arrangement that satisfies these conditions.

Constraints:
- 2 <= nums.length <= 10^3
- nums.length is even
- Half of the integers in nums are even
- 0 <= nums[i] <= 1000

Example 1:
Input: nums = [4, 2, 5, 7]
Output: [4, 5, 2, 7] (or any valid arrangement)
Explanation: [4,5,2,7], [2,5,4,7], [2,7,4,5] are all valid

Example 2:
Input: nums = [2, 3]
Output: [2, 3]
"""

"""
nums = 4 5 2 7
ei = 2 
oi = 1

"""
def sort_array_by_parity_ii(nums):
    # time = O(n)
    # space = O(1)

    ei, oi = 0,1

    while ei < len(nums) -1 and oi < len(nums):
        while ei < len(nums) -1 and nums[ei] % 2 == 0:
            ei += 2
        
        while oi < len(nums) and nums[oi] % 2 == 1:
            oi += 2
        
        if oi < len(nums) and ei < len(nums) -1 :
            nums[oi], nums[ei] = nums[ei], nums[oi]
    
    return nums


def compare_results(result, expected):
    """Custom validator - checks if result satisfies parity constraints"""
    original = expected  # expected holds the original input for validation
    if result is None or len(result) != len(original):
        return False
    if sorted(result) != sorted(original):
        return False  # Must contain same elements
    for i, val in enumerate(result):
        if i % 2 != val % 2:  # index parity must match value parity
            return False
    return True


# Expected = original input (for validation that same elements exist)
TEST_CASES = [
    (([4, 2, 5, 7],), [4, 2, 5, 7]),
    (([2, 3],), [2, 3]),
    (([1, 2, 3, 4, 5, 6],), [1, 2, 3, 4, 5, 6]),
    (([0, 1],), [0, 1]),
    (([3, 4],), [3, 4]),
    (([2, 1, 4, 3, 6, 5],), [2, 1, 4, 3, 6, 5]),
    (([1, 0, 3, 2],), [1, 0, 3, 2]),
]

# For runner.py compatibility
solution = sort_array_by_parity_ii
