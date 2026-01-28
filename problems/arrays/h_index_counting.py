"""
Problem: H-Index (Counting Sort Approach)
Difficulty: Medium

You are given an array of integers citations, where each element citations[i]
represents the number of citations received for the ith publication of a researcher.

Your task is to find the researcher's h-index and return the value of h.

Note: The h-index is defined as the highest number h such that the given researcher
has published at least h papers, each of which has been cited at least h times.

Example 1:
Input: citations = [3, 0, 6, 1, 5]
Output: 3
Explanation: The researcher has 5 papers with [3, 0, 6, 1, 5] citations.
             3 papers have at least 3 citations each (3, 6, and 5).
             So h-index = 3.

Example 2:
Input: citations = [1, 3, 1]
Output: 1
Explanation: The researcher has 3 papers with [1, 3, 1] citations.
             Only 1 paper has at least 1 citation.
             So h-index = 1.

Constraints:
- n == citations.length
- 1 <= n <= 1000
- 0 <= citations[i] <= 1000

Goal: Solve in O(n) time using counting sort / bucket approach
"""


"""
citations = 3 5 10 15 2 34 125
count = 0 1 1 0 1 0 4 

i = 4
hind = 4


citations = 1 3 1
count = 2 0 1 

i = 1
hind = 1

citations = 0
count = 0

i = 0
hind = 0

citations = 100
count = 1
i = 0
hind = 0 
"""

def solution(citations: list[int]) -> int:
    #time = O(n)
    #space = O(n)
    count = [0] * (len(citations) + 1) # n

    for c in citations: #n
        count[min(c, len(citations))] += 1

    i = len(count) -1 
    hind = 0

    while i >=0 : #n
        hind += count[i]
        if hind >= i:
            return i
        i -= 1
    return 0
        


TEST_CASES = [
    (([3, 0, 6, 1, 5],), 3),
    (([1, 3, 1],), 1),
    (([100],), 1),
    (([0],), 0),
    (([0, 0, 0],), 0),
    (([1, 1, 1, 1],), 1),
    (([4, 4, 4, 4],), 4),
    (([10, 8, 5, 4, 3],), 4),
    (([25, 8, 5, 3, 3],), 3),
]
