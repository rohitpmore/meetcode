"""
Problem: Meeting Rooms II
Difficulty: Medium
Source: LeetCode #253

We are given an input array of meeting time intervals, where each interval
has a start time and an end time. Your task is to find the minimum number
of meeting rooms required to hold these meetings.

An important thing to note is that the specified end time for each meeting
is exclusive.

Example 1:
Input: intervals = [[0, 30], [5, 10], [15, 20]]
Output: 2
Explanation: We need 2 rooms:
- Room 1: [0,30]
- Room 2: [5,10], then [15,20]

Example 2:
Input: intervals = [[7, 10], [2, 4]]
Output: 1
Explanation: Meetings don't overlap, so only 1 room needed.

Example 3:
Input: intervals = [[1, 5], [2, 3], [3, 4], [4, 6]]
Output: 2
Explanation: [1,5] conflicts with [2,3] at time 2-3.
But [3,4] can reuse room after [2,3] ends.

Constraints:
- 1 <= intervals.length <= 10^3
- 0 <= start_i < end_i <= 10^6
"""

from typing import List

""" 
    intervals -> [1,6],[4,7],[2,8],[10,12]
    sorted -> [1,6],[2,8], [4,7],[10,12]
    
    mr -> 3
    i -> 2
    L -> 4
    cur_start -> 4
    cur_end -> 6
    mr1 -> 1,6 + 10,12
    mr2 -> 2,8
    mr3 -> 4,7
    
    intervals -> [1,6], [2,8], [7,10]
    mr -> 2
    i -> 1
    L -> 3
    cur_start -> 2
    cur_end -> 6

    intervals -> [7,10], [2,4]
    sorted -> [2,4], [7,10]
    mr -> 1
    i -> 0
    L -> 2
    cur_start -> 2
    cur_end -> 4

    mr1 -> 1,6 + 7,10
    mr2 -> 2,8

    intervals -> [0, 30], [5, 10], [15, 20]
    mr -> 2
    i -> 1
    L -> 3
    cur_start -> 5
    cur_end -> 10

"""
import heapq

def solution(intervals: List[List[int]]) -> int:

    if len(intervals) == 1: 
        return 1

    intervals.sort()
    rooms = []
    maxrooms = 0
    heapq.heapify(rooms)
    heapq.heappush(rooms, intervals[0][1])

    i = 1
    
    while i < len(intervals):
        if rooms[0] > intervals[i][0]:
            heapq.heappush(rooms, intervals[i][1])
        else:
            heapq.heappop(rooms)
            heapq.heappush(rooms, intervals[i][1])
        
        maxrooms = max(maxrooms, len(rooms))
        i += 1

    return maxrooms


TEST_CASES = [
    (([[0, 30], [5, 10], [15, 20]],), 2),
    (([[7, 10], [2, 4]],), 1),
    (([[1, 5], [2, 3], [3, 4], [4, 6]],), 2),
    (([[1, 5]],), 1),  # Single meeting
    (([[1, 3], [3, 5], [5, 7]],), 1),  # Sequential meetings (no overlap)
    (([[1, 4], [2, 5], [3, 6]],), 3),  # All overlap at time 3
    (([[0, 5], [1, 2], [1, 3], [1, 4]],), 4),  # Maximum overlap
]
