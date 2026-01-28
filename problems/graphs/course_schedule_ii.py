"""
Problem: Course Schedule II
Difficulty: Medium

You are given n courses, labeled from 0 to n - 1. Some courses have prerequisites,
which are provided as a list of pairs: prerequisites[i] = [a, b]. To take course a,
you must first complete course b.

Your task is to determine a valid order in which you can complete all the courses
and return it as an array of course labels.

If there are multiple valid orderings, you can return any of them.
If it's impossible to finish all courses (due to a cycle in prerequisites),
return an empty array.

Note: There can be a course in the 0 to n-1 range with no prerequisites.

Constraints:
- 1 <= n <= 1500
- 0 <= prerequisites.length <= 1000
- prerequisites[i].length == 2
- 0 <= a, b < n
- a != b
- All the pairs [a, b] are distinct.

Example 1:
Input: n = 4, prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
Output: [0, 1, 2, 3] or [0, 2, 1, 3]
Explanation: Course 0 has no prerequisites. Courses 1 and 2 both need 0.
             Course 3 needs both 1 and 2. Multiple valid orderings exist.

Example 2:
Input: n = 2, prerequisites = [[1, 0], [0, 1]]
Output: []
Explanation: Cycle exists, impossible to complete.
"""

from collections import deque

def solution(n: int, prerequisites: list[list[int]]) -> list[int]:
    indegrees = {}
    adj = {}

    for i in range(n):
        indegrees[i] = 0
        adj[i] = []

    for dep in prerequisites:
        indegrees[dep[0]] += 1
        adj[dep[1]].append(dep[0])

    q = deque()

    for k in indegrees:
        if indegrees[k] == 0:
            q.append(k)
    res = []
    while len(q) != 0 :
        k = q.popleft()
        res.append(k)
        for a in adj[k]:
            indegrees[a] -= 1
            if indegrees[a] == 0 :
                q.append(a)
    
    if len(res) != n:
        return []
    else:
        return res

# Comparator for runner: accepts any valid ordering (same courses)
def compare_results(result: list[int], expected: list[int]) -> bool:
    # Cycle case: both must be empty
    if expected == []:
        return result == []
    # Otherwise: must contain the same courses
    return sorted(result) == sorted(expected)


TEST_CASES = [
    # Basic cases
    ((2, [[1, 0]]), [0, 1]),                              # Simple: 0 -> 1
    ((2, [[1, 0], [0, 1]]), []),                          # Cycle: impossible

    # No prerequisites
    ((3, []), [0, 1, 2]),                                  # Any order valid
    ((1, []), [0]),                                        # Single course

    # Chain dependencies
    ((3, [[1, 0], [2, 1]]), [0, 1, 2]),                   # Linear: 0 -> 1 -> 2
    ((4, [[1, 0], [2, 1], [3, 2]]), [0, 1, 2, 3]),        # Longer chain

    # Diamond shape (multiple valid orderings)
    ((4, [[1, 0], [2, 0], [3, 1], [3, 2]]), [0, 1, 2, 3]), # 0 -> {1,2} -> 3

    # Multiple prereqs
    ((3, [[2, 0], [2, 1]]), [0, 1, 2]),                   # 2 needs both 0 and 1

    # Cycles
    ((3, [[0, 1], [1, 2], [2, 0]]), []),                  # 3-node cycle
    ((4, [[0, 1], [1, 2], [2, 3], [3, 0]]), []),          # 4-node cycle

    # Disconnected components
    ((4, [[1, 0], [3, 2]]), [0, 1, 2, 3]),                # Two separate chains
]

