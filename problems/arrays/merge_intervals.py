"""
Problem: Merge Intervals
Difficulty: Medium
Source: LeetCode #56

We are given an array of closed intervals called intervals, where each interval
has a start time and an end time and is represented as intervals[i] = [starti, endi].
Your task is to merge the overlapping intervals and return a new output array
consisting of only the non-overlapping intervals.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:
- 1 <= intervals.length <= 10^3
- intervals[i].length == 2
- 0 <= starti <= endi <= 10^4
"""

from typing import List

""" 
intervals -> [[1,4], [1,5]]
sorted -> [[1,4], [1,5]]
output -> [[1,5]]
cur_start -> 1
cur_end -> 5
i -> 1

intervals -> [[1,4], [5,8], [3,5],[11,20], [9,12]]
sorted -> [[1,4],[3,5],[5,8],[9,12],[11,20]]
output -> [[1,8],[9,20]]
cur_start -> 9
cur_end -> 20
i -> 4
L -> 5

intervals -> [[1, 3], [2, 6], [8, 10], [15, 18]]
sorted -> [1,3], [2,6],[8,10],[15,18]

output -> [[1,6],]
cur_start -> 8
cur_end -> 10

i -> 0
"""

def solution(intervals: List[List[int]]) -> List[List[int]]:

    if len(intervals) == 1 :
        return intervals
    
    intervals.sort()
    output = []
    cur_start, cur_end = -1, -1

    for i in range(len(intervals)-1):
        if cur_start == -1:
            cur_start = intervals[i][0]
        if cur_end == -1:
            cur_end = intervals[i][1]

        if cur_end >= intervals[i+1][0]:
            cur_end = max(cur_end, intervals[i+1][1])
        else:
            output.append([cur_start, cur_end])
            cur_start = intervals[i+1][0]
            cur_end = intervals[i+1][1]

    output.append([cur_start, cur_end])
    return output


TEST_CASES = [
    (([[1, 3], [2, 6], [8, 10], [15, 18]],), [[1, 6], [8, 10], [15, 18]]),
    (([[1, 4], [4, 5]],), [[1, 5]]),
    (([[1, 4], [0, 4]],), [[0, 4]]),
    (([[1, 4], [2, 3]],), [[1, 4]]),  # One interval completely inside another
    (([[1, 4]],), [[1, 4]]),  # Single interval
    (([[1, 4], [0, 0]],), [[0, 0], [1, 4]]),  # Non-overlapping
    (([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]],), [[1, 10]]),  # One large interval covers all
]
