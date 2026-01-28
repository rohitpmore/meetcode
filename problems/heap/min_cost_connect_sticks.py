"""
Problem: Minimum Cost to Connect Sticks
Difficulty: Medium

You are given a set of sticks with positive integer lengths represented as an
array, sticks, where sticks[i] denotes the length of the i-th stick.

You can connect any two sticks into one stick at a cost equal to the sum of
their lengths. Once two sticks are combined, they form a new stick whose length
is the sum of the two original sticks. This process continues until there is
only one stick remaining.

Your task is to determine the minimum cost required to connect all the sticks
into a single stick.

Constraints:
- 1 <= sticks.length <= 10^3
- 1 <= sticks[i] <= 10^3

Example 1:
Input: sticks = [2, 4, 3]
Output: 14
Explanation:
- Combine 2 + 3 = 5, cost = 5, sticks = [4, 5]
- Combine 4 + 5 = 9, cost = 9, sticks = [9]
- Total cost = 5 + 9 = 14

Example 2:
Input: sticks = [1, 8, 3, 5]
Output: 30
Explanation:
- Combine 1 + 3 = 4, cost = 4, sticks = [4, 5, 8]
- Combine 4 + 5 = 9, cost = 9, sticks = [8, 9]
- Combine 8 + 9 = 17, cost = 17, sticks = [17]
- Total cost = 4 + 9 + 17 = 30

Example 3:
Input: sticks = [5]
Output: 0
Explanation: Only one stick, no combining needed.
"""

from typing import List
import heapq

def solution(sticks: List[int]) -> int:
    """
    Find the minimum cost to connect all sticks into one.

    Args:
        sticks: List of stick lengths

    Returns:
        int: Minimum total cost to combine all sticks
    """
    if len(sticks) == 1:
        return 0
    
    heapq.heapify(sticks)
    cost = 0

    while len(sticks) > 1:
        st1 = heapq.heappop(sticks)
        st2 = heapq.heappop(sticks)
        cost += (st1 + st2)
        heapq.heappush(sticks, st1+st2)
    
    return cost

    

TEST_CASES = [
    (([2, 4, 3],), 14),
    (([1, 8, 3, 5],), 30),
    (([5],), 0),  # Single stick - no cost
    (([1, 1, 1, 1],), 8),  # All same length: (1+1)=2, (1+1)=2, (2+2)=4 → 2+2+4=8
    (([3, 4, 5, 6],), 36),  # (3+4)=7, (5+6)=11, (7+11)=18 → 7+11+18=36
    (([1, 2],), 3),  # Two sticks
]
