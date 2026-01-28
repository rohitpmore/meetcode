"""
Problem: Valid Triangle Number
Difficulty: Medium

Given an array of integers, nums, determine the number of unique triplets that can
be selected from the array such that the selected values can form the sides of a
valid triangle. Return this count as the result.

Triangle Validity Rule:
For three sides a, b, c to form a valid triangle:
- a + b > c
- a + c > b
- b + c > a

Example 1:
Input: nums = [2, 2, 3, 4]
Output: 3
Explanation: Valid triplets are:
             - nums[0], nums[1], nums[2] → (2, 2, 3): 2+2 > 3 ✓
             - nums[0], nums[2], nums[3] → (2, 3, 4): 2+3 > 4 ✓
             - nums[1], nums[2], nums[3] → (2, 3, 4): 2+3 > 4 ✓
             Note: (2, 2, 4) invalid since 2+2 = 4, not > 4

Example 2:
Input: nums = [4, 2, 3, 4]
Output: 4

Constraints:
- 1 <= nums.length <= 1000
- 0 <= nums[i] <= 1000
"""

"""
nums = 3 5 7 9 12

k = 4
i = 0, j = 3
i = 1, j = 3, add +2
i = 1, j = 2
"""
def solution(nums: list[int]) -> int:

    # time = O(n^2)
    # space = O(n) because of Tim sort
    if len(nums) < 3:
        return 0

    nums.sort() # nlogn
    
    k = len(nums) - 1
    count = 0

    while k >= 2: #n
        i = 0
        j = k-1

        while i < j: #n
            if nums[i] + nums[j] > nums[k]:
                count += (j-i)
                j -= 1
            else:
                i += 1

        k -= 1        

    return count


TEST_CASES = [
    (([2, 2, 3, 4],), 3),
    (([4, 2, 3, 4],), 4),
    (([1, 1, 1, 1],), 4),
    (([1, 2, 3],), 0),
    (([0, 0, 0],), 0),
    (([7, 0, 0, 0],), 0),
    (([3, 4, 5, 6, 7],), 9),
    (([1],), 0),
    (([1, 2],), 0),
]
