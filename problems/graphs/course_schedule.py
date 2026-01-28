"""
Problem: Course Schedule
Difficulty: Medium

You are given an integer, num_courses, representing the total number of courses
you need to complete, labeled from 0 to num_courses - 1.

You are also given a prerequisites array, where prerequisites[i] = [a[i], b[i]]
indicates that you must take course b[i] first if you want to take the course a[i].
For example, the pair [1, 0] indicates that to take course 1, you have to first
take course 0.

Return TRUE if all of the courses can be finished. Otherwise, return FALSE.

Constraints:
- 1 <= num_courses <= 1500
- 0 <= prerequisites.length <= 1000
- prerequisites[i].length == 2
- 0 <= a[i], b[i] < num_courses
- All the pairs prerequisites[i] are unique.

Example 1:
Input: num_courses = 2, prerequisites = [[1, 0]]
Output: True
Explanation: You can take course 0 first, then course 1.

Example 2:
Input: num_courses = 2, prerequisites = [[1, 0], [0, 1]]
Output: False
Explanation: To take course 1, you need course 0. To take course 0, you need course 1.
             This creates a cycle, so it's impossible.
"""

"""
num_courses = 5
prerequisites = [4,3],[4,2],[3,2],[3,1],[1,0]

indegree = 0:0, 1:0, 2:0, 3:0, 4:0
adj = 0:{1}, 1:{3}, 2:{4,3}, 3:{4}, 4:{}, 5:{}

q =  
completed = 5

num_courses = 5
prerequisites = [4,3],[2,4],[3,2],[3,1],[1,0]

indegree = 0:0, 1:0, 2:1, 3:1, 4:1
adj = 0:{1}, 1:{3}, 2:{3}, 3:{4}, 4:{2}, 5:{}

q = 
completed = 2


"""
from collections import deque
def solution(num_courses: int, prerequisites: list[list[int]]) -> bool:

    # time = O(V + E)
    # space = O(V + E)
    if len(prerequisites) == 0:
        return True
    
    indegree = {}
    adj = {}
    

    for i in range(num_courses):
        indegree[i] = 0
        adj[i] = []

    for dep in prerequisites:
        indegree[dep[0]] += 1
        adj[dep[1]].append(dep[0])
    
    q = deque()

    for k in indegree.keys():
        if indegree.get(k) == 0 :
            q.append(k)
    completed = 0
    while len(q) != 0 :
        k = q.popleft()
        completed += 1
        for c in adj[k]:
            indegree[c] -= 1
            if indegree[c] == 0 :
                q.append(c)
    

    if completed < num_courses:
        return False
    else:
        return True
        

        



TEST_CASES = [
    # Basic cases
    ((2, [[1, 0]]), True),                          # Simple dependency: 0 -> 1
    ((2, [[1, 0], [0, 1]]), False),                 # Cycle between 2 courses

    # No prerequisites
    ((5, []), True),                                 # No dependencies, all completable
    ((1, []), True),                                 # Single course, no deps

    # Chain dependencies
    ((3, [[1, 0], [2, 1]]), True),                  # Linear chain: 0 -> 1 -> 2
    ((4, [[1, 0], [2, 1], [3, 2]]), True),          # Longer chain: 0 -> 1 -> 2 -> 3

    # Complex graphs
    ((4, [[1, 0], [2, 0], [3, 1], [3, 2]]), True),  # Diamond shape, no cycle
    ((3, [[0, 1], [0, 2], [1, 2]]), True),          # Multiple prereqs for one course

    # Cycles of different sizes
    ((3, [[0, 1], [1, 2], [2, 0]]), False),         # 3-node cycle
    ((4, [[0, 1], [1, 2], [2, 3], [3, 0]]), False), # 4-node cycle

    # Self-loop (edge case)
    ((2, [[0, 0]]), False),                          # Course requires itself
]
