"""
Problem: Find the Corrupt Pair
Difficulty: Medium
Time Limit: 30 min

Description:
We are given an unsorted array, nums, with n elements and each element
is in the range [1, n] inclusive. The array originally contained all
the elements from 1 to n but due to a data error, one of the numbers
is duplicated, which causes another number to be missing.

Find and return the corrupt pair (missing, duplicated).

Constraints:
- 2 <= n <= 10^3
- 1 <= nums[i] <= n

Example 1:
Input: nums = [3, 1, 2, 5, 2]
Output: (4, 2)
Explanation: 2 appears twice, and 4 is missing from [1,2,3,4,5]

Example 2:
Input: nums = [3, 1, 2, 3, 6, 4]
Output: (5, 3)
Explanation: 3 appears twice, and 5 is missing from [1,2,3,4,5,6]
"""

"""
nums = 5 1 3 4 5 
i = 1

"""
def find_corrupt_pair(nums):

    # time = O(n)
    # space = O(1)

    i = 0
    while i < len(nums):
        if (i + 1) != nums[i] and nums[i] != nums[nums[i]-1]:
            t = nums[i] - 1
            nums[i], nums[t] =  nums[t] , nums[i]
        else:
            i += 1

    i = 0 
    for i in range(len(nums)):
        if (i+1) != nums[i]:
            return [i+1, nums[i]]






TEST_CASES = [
    # (input, expected_output)
    (([3, 1, 2, 5, 2],), [4, 2]),
    (([3, 1, 2, 3, 6, 4],), [5, 3]),
    (([1, 1],), [2, 1]),
    (([2, 2],), [1, 2]),
    (([4, 1, 2, 1, 6, 3],), [5, 1]),
    (([1, 5, 3, 6, 4, 6, 2],), [7, 6]),
]

# For runner.py compatibility
solution = find_corrupt_pair
