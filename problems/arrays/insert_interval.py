"""
Problem: Insert Interval
Difficulty: Medium

You are given a list of non-overlapping intervals, intervals, where each interval
is represented as [starti, endi] and the list is sorted in ascending order by
the start of each interval (starti). You are also given another interval,
new_interval = [start, end].

Your task is to insert new_interval into the list of intervals such that the
list remains sorted by starting times and still contains no overlapping intervals.
If any intervals overlap after the insertion, merge them accordingly.

Return the updated list of intervals.

Note: You don't need to modify intervals in place. You can make a new array and return it.

Constraints:
- 0 <= intervals.length <= 10^4
- intervals[i].length, new_interval.length == 2
- 0 <= starti < endi <= 10^4
- The list of intervals is sorted in ascending order based on the start time.

Example 1:
Input: intervals = [[1,3],[6,9]], new_interval = [2,5]
Output: [[1,5],[6,9]]
Explanation: The new interval [2,5] overlaps with [1,3], so they merge into [1,5].

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], new_interval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: The new interval [4,8] overlaps with [3,5],[6,7],[8,10], merging into [3,10].

Example 3:
Input: intervals = [], new_interval = [5,7]
Output: [[5,7]]
"""

def solution(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    # TODO(human): Implement your solution
    if len(intervals) == 0 : 
        return [new_interval]
    
    output = []

    new_start, new_end = new_interval[0],new_interval[1]
    i = 0

    # Loop 1: Add all intervals that come BEFORE new_interval (no overlap)
    while i < len(intervals) and intervals[i][1] < new_start:
        output.append(intervals[i])
        i += 1

    # Loop 2: Merge all overlapping intervals into new_interval
    while i < len(intervals) and intervals[i][0] <= new_end:
        new_start = min(new_start, intervals[i][0])
        new_end = max(new_end, intervals[i][1])
        i += 1

    output.append([new_start,new_end])

    # Loop 3: Add all remaining intervals (they come AFTER the merged interval)
    while i < len(intervals):
        output.append(intervals[i])
        i += 1

    return output
        
        

    

TEST_CASES = [
    # (input_args, expected_output)
    (([[1, 3], [6, 9]], [2, 5]), [[1, 5], [6, 9]]),
    (([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]), [[1, 2], [3, 10], [12, 16]]),
    (([], [5, 7]), [[5, 7]]),
    (([[1, 5]], [2, 3]), [[1, 5]]),  # new_interval fully inside existing
    (([[1, 5]], [0, 6]), [[0, 6]]),  # new_interval fully covers existing
    (([[1, 5]], [6, 8]), [[1, 5], [6, 8]]),  # no overlap, insert after
    (([[3, 5]], [1, 2]), [[1, 2], [3, 5]]),  # no overlap, insert before
    (([[1, 2], [5, 6]], [3, 4]), [[1, 2], [3, 4], [5, 6]]),  # insert in middle, no overlap
]
