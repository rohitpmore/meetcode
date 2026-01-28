"""
Problem: Find K Pairs with Smallest Sums
Difficulty: Medium

You are given two integer arrays, list1 and list2, sorted in non-decreasing order,
and an integer k.

A pair (u, v) is defined as one element u chosen from list1 and one element v
chosen from list2.

Your task is to return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) whose sums
u1+v1, u2+v2, ..., uk+vk are the smallest among all possible such pairs.

Constraints:
- 1 <= list1.length, list2.length <= 500
- -10^4 <= list1[i], list2[i] <= 10^4
- 1 <= k <= 10^3
- Input lists are sorted in ascending order
- If k exceeds total valid pairs, return all pairs

Example 1:
Input: list1 = [1,7,11], list2 = [2,4,6], k = 3
Output: [[1,2], [1,4], [1,6]]
Explanation: The first 3 pairs are returned from the sequence:
[1,2], [1,4], [1,6], [7,2], [7,4], [11,2], [7,6], [11,4], [11,6]

Example 2:
Input: list1 = [1,1,2], list2 = [1,2,3], k = 2
Output: [[1,1], [1,1]]
Explanation: The first 2 pairs are returned from the sequence:
[1,1], [1,1], [1,2], [2,1], [1,2], [1,3], [2,2], [2,3]

Example 3:
Input: list1 = [1,2], list2 = [3], k = 3
Output: [[1,3], [2,3]]
Explanation: All possible pairs are returned since k > total pairs.
"""

from heapq import *

def solution(list1: list[int], list2: list[int], k: int) -> list[list[int]]:
    """
    list1 = 1,2,3,4,5,6,7,8
    list2 = 2,4,6,8,10,12,14,16
    k = 4
    c = 3

    mh = [5,0,1],[6,2,0],[8,1,2],[7,2,1]
    result = [1,2],[2,2],[4,2]
    l1 = 1
    l2 = 1
    """

    mh = []
    heapify(mh)
    c = 0
    result = []

    i = 0
    while i < len(list1) and c < k :
        heappush(mh, [list1[i] + list2[0], i, 0])
        c += 1
        i += 1

    c = 0

    while len(mh) > 0 and c < k:
        _, l1, l2 = heappop(mh)
        if l2 < len(list2) - 1:
            heappush(mh, [list1[l1] + list2[l2+1], l1,l2+1])
        result.append([list1[l1],list2[l2]])
        c += 1

    return result



# Test cases: ((list1, list2, k), expected_output)
TEST_CASES = [
    (([1, 7, 11], [2, 4, 6], 3), [[1, 2], [1, 4], [1, 6]]),
    (([1, 1, 2], [1, 2, 3], 2), [[1, 1], [1, 1]]),
    (([1, 2], [3], 3), [[1, 3], [2, 3]]),
    (([1, 2, 3], [1, 2, 3], 5), [[1, 1], [1, 2], [2, 1], [1, 3], [2, 2]]),
    (([1], [1], 1), [[1, 1]]),
    # Larger test - should have exactly 9 unique pairs, no duplicates
    (([1, 2, 3], [1, 2, 3], 9), [[1, 1], [1, 2], [2, 1], [1, 3], [2, 2], [3, 1], [2, 3], [3, 2], [3, 3]]),
]
