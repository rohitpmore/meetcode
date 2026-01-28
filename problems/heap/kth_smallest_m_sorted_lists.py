"""
Problem: Kth Smallest Number in M Sorted Lists
Difficulty: Medium

Given a list, lists, containing m sorted lists of integers in ascending order,
and an integer k, find the kth smallest element among all the lists.

Even if some values appear multiple times across the lists, each occurrence is
treated as a unique element when determining the kth smallest number.

If k exceeds the total number of elements across all lists, return the largest
element among them. If the lists are empty, return 0.

Constraints:
- 1 <= m <= 50
- 0 <= lists[i].length <= 50
- -10^9 <= lists[i][j] <= 10^9
- 1 <= k <= 10^9

Example 1:
Input: lists = [[2, 6, 8], [3, 6, 10], [5, 8, 11]], k = 5
Output: 6
Explanation: Combined sorted: [2, 3, 5, 6, 6, 8, 8, 10, 11], 5th element is 6.

Example 2:
Input: lists = [[1, 2, 3], [4, 5], [6]], k = 4
Output: 4
Explanation: Combined sorted: [1, 2, 3, 4, 5, 6], 4th element is 4.

Example 3:
Input: lists = [[1], [2], [3, 100]], k = 10
Output: 100
Explanation: k=10 exceeds total elements (4), return largest element 100.

Example 4:
Input: lists = [[], [], []], k = 1
Output: 0
Explanation: All lists empty, return 0.
"""

"""
lists = 
    [
        [1,2,3,4,5],
        [2,3],
        [],
        [10,11,12]
    ]
k = 5
mh = [10,2,0], [3,0,2], [4,0,3]
c = 5
elem = 3
li = 0
ei = 2

Time - O(k logm)
Space - O(log m)
"""
from heapq import heapify, heappop, heappush

def solution(lists: list[list[int]], k: int) -> int:
    mh = []
    heapify(mh)

    for i in range(len(lists)):
        if len(lists[i]) > 0 :
            heappush(mh, [lists[i][0],i, 0])
    
    c = 0
    elem = 0

    while len(mh) > 0 and c < k:
        elem, li, ei = heappop(mh)
        if ei + 1 < len(lists[li]):
            heappush(mh, [lists[li][ei+1], li, ei + 1])
        c += 1

    return elem


    

# Test cases: ((lists, k), expected_output)
TEST_CASES = [
    (([[2, 6, 8], [3, 6, 10], [5, 8, 11]], 5), 6),
    (([[1, 2, 3], [4, 5], [6]], 4), 4),
    (([[1], [2], [3, 100]], 10), 100),  # k exceeds total, return largest
    (([[], [], []], 1), 0),  # All empty lists
    (([[1, 1, 1], [1, 1, 1]], 4), 1),  # All same values
    (([[-5, -3, -1], [0, 2, 4]], 3), -1),  # Negative numbers
    (([[10]], 1), 10),  # Single element
    (([[1, 5], [2, 3], [4, 6]], 6), 6),  # Multiple lists, exact k
]
