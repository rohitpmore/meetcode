"""
Problem: Exclusive Time of Functions
Difficulty: Medium

We are given an integer number n, representing the number of functions running
in a single-threaded CPU, and an execution log (a list of strings). Each string
has the format: {function_id}:{"start" | "end"}:{timestamp}

This indicates that the function with function_id either started or stopped
execution at the time identified by the timestamp value.

Each function has a unique ID between 0 and n-1.

Compute the exclusive time of each function in the program.

Note: The exclusive time is the sum of execution times for all calls to a
specific function. A "start" timestamp means the function begins at the START
of that time unit. An "end" timestamp means the function finishes at the END
of that time unit.

Example 1:
Input: n = 2, logs = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
Output: [3, 4]
Explanation:
- Function 0 runs during time units [0,1] and [6] = 3 units
- Function 1 runs during time units [2,3,4,5] = 4 units

Example 2:
Input: n = 1, logs = ["0:start:0", "0:end:0"]
Output: [1]
Explanation: Function 0 runs from start to end of time unit 0 = 1 unit

Example 3:
Input: n = 2, logs = ["0:start:0", "1:start:1", "1:end:1", "0:end:2"]
Output: [2, 1]
Explanation:
- Function 0 runs during [0] and [2] = 2 units
- Function 1 runs during [1] = 1 unit

Example 4 (nested calls):
Input: n = 3, logs = ["0:start:0", "1:start:1", "2:start:2", "2:end:3", "1:end:4", "0:end:5"]
Output: [2, 2, 2]
Explanation:
- Function 0: units [0] and [5] = 2
- Function 1: units [1] and [4] = 2
- Function 2: units [2,3] = 2

Constraints:
- 1 <= n <= 100
- 1 <= logs.length <= 500
- 0 <= function_id < n
- 0 <= timestamp <= 1000
- No two start events or two end events happen at the same timestamp
- Each function has an end log for each start log
"""

from typing import List
from collections import deque


def exclusive_time(n: int, logs: List[str]) -> List[int]:
    """
    Return a list of length n where result[i] is the exclusive time of function i.
    """

    # time = O(S)
    # space = O(n + s)

    result = [0] * n
    st = deque()
    prev_time = 0

    for l in logs:
        [fid, kw, ts] = l.split(':')

        if kw  == "start":
            if len(st) > 0:
                result[st[-1]] += int(ts) - prev_time
            st.append(int(fid))
            prev_time = int(ts)
        
        if kw == "end":
            result[st[-1]] += int(ts) - prev_time + 1
            st.pop()
            prev_time = int(ts) + 1
    
    return result



# Alias for test runner
solution = exclusive_time


TEST_CASES = [
    ((2, ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]), [3, 4]),
    ((1, ["0:start:0", "0:end:0"]), [1]),
    ((2, ["0:start:0", "1:start:1", "1:end:1", "0:end:2"]), [2, 1]),
    ((3, ["0:start:0", "1:start:1", "2:start:2", "2:end:3", "1:end:4", "0:end:5"]), [2, 2, 2]),
    ((1, ["0:start:0", "0:start:2", "0:end:3", "0:end:4"]), [5]),  # Recursive call
    ((2, ["0:start:0", "0:end:1", "1:start:2", "1:end:3"]), [2, 2]),  # Sequential, no nesting
]
