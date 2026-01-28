"""
Problem: Schedule Tasks on Minimum Machines
Difficulty: Medium

We are given an input array, tasks, where tasks[i] = [start_i, end_i]
represents the start and end times of n tasks. Our goal is to schedule
these tasks on machines given the following criteria:

- A machine can execute only one task at a time.
- A machine can begin executing a new task immediately after completing
  the previous one (if task A ends at time 5, task B can start at time 5).
- An unlimited number of machines are available.

Find the minimum number of machines required to complete these n tasks.

Constraints:
- 1 <= tasks.length <= 10^3
- 0 <= tasks[i][0] < tasks[i][1] <= 10^4

Example 1:
Input: tasks = [[1, 7], [8, 13], [5, 6], [10, 14], [6, 7]]
Output: 2

Example 2:
Input: tasks = [[1, 3], [3, 5], [5, 7]]
Output: 1
Explanation: No overlaps - tasks can run sequentially on one machine.

Example 3:
Input: tasks = [[1, 5], [2, 6], [3, 7]]
Output: 3
Explanation: All three tasks overlap, so 3 machines needed.
"""

from typing import List
import heapq

def solution(tasks: List[List[int]]) -> int:
    """
    Find the minimum number of machines required to execute all tasks.

    Args:
        tasks: List of [start, end] intervals representing task times

    Returns:
        int: Minimum number of machines needed
    """
    """
    s-tasks = [1,5],[5,10],[8,12], [11,25],[12,14],[15,20]
    machines = [14,25]
    mm = 2
    i = 5




    """
    if len(tasks) == 1:
        return 1
    
    machines = []
    mm = 0
    heapq.heapify(machines)
    tasks.sort()

    for i in range(len(tasks)):
        if len(machines) == 0:
            heapq.heappush(machines, tasks[i][1])
        else:
            et = machines[0]
            if et > tasks[i][0]:
                heapq.heappush(machines, tasks[i][1])
            else:
                heapq.heappop(machines)
                heapq.heappush(machines, tasks[i][1])
        
        mm = max(mm, len(machines))

    return mm
        
TEST_CASES = [
    (([[1, 7], [8, 13], [5, 6], [10, 14], [6, 7]],), 2),
    (([[1, 3], [3, 5], [5, 7]],), 1),  # Sequential - can reuse machine
    (([[1, 5], [2, 6], [3, 7]],), 3),  # All overlap
    (([[1, 5]],), 1),  # Single task
    (([[0, 5], [1, 2], [1, 3], [1, 4]],), 4),  # Multiple start at same time
    (([[1, 10], [2, 3], [4, 5], [6, 7]],), 2),  # One long task with short ones
]
