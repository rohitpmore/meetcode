"""
Problem: Top K Frequent Elements
Difficulty: Medium
Time Limit: 30 min

Description:
Given an array of integers, arr, and an integer, k, return the k most
frequent elements.

Note: You can return the answer in any order.

Constraints:
- 1 <= arr.length <= 10^3
- -10^4 <= arr[i] <= 10^4
- 1 <= k <= number of unique elements in the array
- It is guaranteed that the answer is unique.

Example 1:
Input: arr = [1, 1, 1, 2, 2, 3], k = 2
Output: [1, 2]
Explanation: 1 appears 3 times, 2 appears 2 times, 3 appears 1 time.
The 2 most frequent are [1, 2].

Example 2:
Input: arr = [1], k = 1
Output: [1]

Example 3:
Input: arr = [4, 4, 4, 6, 6, 6, 6, 1, 1], k = 2
Output: [6, 4]
Explanation: 6 appears 4 times, 4 appears 3 times, 1 appears 2 times.
"""

"""
arr = 1, 2, 3, 4, 5, 4, 3, 3, 1, 5, 5, 10
k = 3

freq = {
        "1": 2,
        "2": 1,
        "3": 3,
        "4": 2,
        "5": 3,
        "10": 1,
    }

mh = [3,5] [2,1]  [3,3]
"""
from typing import List

from heapq import heapify, heappushpop, heappush
def solution(arr: List[int], k: int) -> List[int]:
    # time -> O(n log k)
    # space -> O(n)

    freq = {}

    for i in range(len(arr)):
        freq[arr[i]] = freq.get(arr[i], 0) + 1
    
    mh = []
    heapify(mh)

    for num, f in freq.items():
        if len(mh) < k:
            heappush(mh, [f,num])
        else:
            if mh[0][0] < f:
                _ = heappushpop(mh, [f, num])
    
    return [elem[1] for elem in mh]





TEST_CASES = [
    # (input_args, expected_output)
    (([1, 1, 1, 2, 2, 3], 2), [1, 2]),
    (([1], 1), [1]),
    (([4, 4, 4, 6, 6, 6, 6, 1, 1], 2), [6, 4]),
    (([1, 2, 3, 4], 4), [1, 2, 3, 4]),  # All elements equally frequent
    (([5, 5, 5, 5], 1), [5]),  # Single unique element
    (([1, 2, 2, 3, 3, 3], 1), [3]),  # k=1, return most frequent
    (([-1, -1, -2, -2, -2, 3], 2), [-2, -1]),  # Negative numbers
]
