"""
Problem: Combinations
Difficulty: Medium
Time Limit: 30 min

You are given two integers, n and k. Your task is to return all possible
combinations of k numbers chosen from the range [1, n].

The result can be returned in any order.

Note: Combinations are unordered, i.e., [1, 2] and [2, 1] are considered
the same combination.

Constraints:
- 1 <= n <= 20
- 1 <= k <= n

Example 1:
Input: n = 4, k = 2
Output: [[1,2], [1,3], [1,4], [2,3], [2,4], [3,4]]
Explanation: All possible combinations of 2 numbers from [1,2,3,4]

Example 2:
Input: n = 1, k = 1
Output: [[1]]
Explanation: Only one number, only one combination

Example 3:
Input: n = 5, k = 3
Output: [[1,2,3], [1,2,4], [1,2,5], [1,3,4], [1,3,5], [1,4,5],
         [2,3,4], [2,3,5], [2,4,5], [3,4,5]]
"""
"""
n = 5, k = 3

rec(1,[])
    rec(2,[1])
        rec(3,[1,2])
            rec(4,[1,2,3])
                add to result [1,2,3]
            rec(5,[1,2,4])
                add to result [1,2,4]
            rec(6,[1,2,5])
                add to result [1,2,5]
        rec(4,[1,3])
            rec(5,[1,3,4])
                add to result [1,3,4]
            rec(6,[1,3,5])
                add to result [1,3,5]
        rec(5,[1,4])
            rec(6, [1,4,5])
                add to result [1,4,5]
    rec(3,[2])
        rec(4,[2,3])
            rec(5,[2,3,4])
                add to result [2,3,4]
            rec(6,[2,3,5])
                add to result [2,3,5]
        rec(5,[2,4])
            rec(6, [2,4,5])
                add to result [2,4,5]
    rec(4,[3])
        rec(5,[3,4])
            rec(6, [3,4,5])
                add to result [3,4,5]
    rec(5,[4])


"""

def solution(n: int, k: int) -> list[list[int]]:
    """
    Return all possible combinations of k numbers from range [1, n].
    """
    result = []

    def rec(d, cc):
        if len(cc) == k:
            result.append(list(cc))
            return

        for i in range(d, n+1):
            cc.append(i)
            rec(i+1,cc)
            cc.pop()

    rec(1,[])

    return result



# Custom comparison - order doesn't matter for combinations
def compare_results(actual, expected):
    if actual is None or expected is None:
        return actual == expected
    # Sort each combination and then sort the list of combinations
    actual_sorted = sorted([sorted(combo) for combo in actual])
    expected_sorted = sorted([sorted(combo) for combo in expected])
    return actual_sorted == expected_sorted


TEST_CASES = [
    # (input_args, expected_output)
    # Example 1: n=4, k=2
    ((4, 2), [[1,2], [1,3], [1,4], [2,3], [2,4], [3,4]]),

    # Example 2: Single element
    ((1, 1), [[1]]),

    # k equals n - only one combination
    ((3, 3), [[1, 2, 3]]),

    # k = 1 - each number is its own combination
    ((4, 1), [[1], [2], [3], [4]]),

    # Larger example
    ((5, 3), [[1,2,3], [1,2,4], [1,2,5], [1,3,4], [1,3,5],
              [1,4,5], [2,3,4], [2,3,5], [2,4,5], [3,4,5]]),

    # Edge case: n=2, k=1
    ((2, 1), [[1], [2]]),

    # Edge case: n=2, k=2
    ((2, 2), [[1, 2]]),
]
