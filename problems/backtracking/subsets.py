"""
Problem: Subsets
Difficulty: Medium
Time Limit: 30 min

Given an array of integers, nums, find all possible subsets of nums, including the empty set.

Note: The solution set must not contain duplicate subsets. You can return the solution in any order.

Constraints:
- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10
- All the numbers of nums are unique.

Example 1:
Input: nums = [1, 2, 3]
Output: [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]

Example 2:
Input: nums = [0]
Output: [[], [0]]

Example 3:
Input: nums = [1, 2]
Output: [[], [1], [2], [1, 2]]
"""

"""
[]
    [1]
        [1,2]
            [1,2,3]
        [1,3]
    [2]
        [2,3]
    [3]
    
"""

"""
nums = [1,2,3]

result = [
            [],
            [1],
            [2],
            [3],
            [1,2],
            [1,3],
            [2,3],
            [1,2,3]
            ]

rec([], [1,2,3])
    rec([1], [2,3])
        rec([1,2], [3])
            rec([1,2,3], [])
                .
        rec([1,3],[])
            .
    rec([2], [3])
        rec([2,3], [])
            .
    rec([3], [])
        .


"""
def solution(nums: list[int]) -> list[list[int]]:
    # time = O(n 2^n)
    # space = O(n 2^n) if we include result as well in space calculations..  recustion stack O(n^2)
    result = []

    def rec(cur, remaining):
        result.append(cur)
        if len(remaining) == 0 :
            return
        else:
            for i, r in enumerate(remaining):
                rec(cur + [r], remaining[i+1:])

    
    rec([], nums)
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
    # Convert lists to tuples for set comparison
    result_set = {tuple(sorted(x)) for x in result}
    expected_set = {tuple(sorted(x)) for x in expected}
    return result_set == expected_set
