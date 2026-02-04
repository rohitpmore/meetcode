"""
Problem: Graph Valid Tree
Difficulty: Medium

Given n as the number of nodes and an array of the edges of a graph,
find out if the graph is a valid tree. The nodes of the graph are
labeled from 0 to n-1, and edges[i] = [x, y] represents an undirected
edge connecting the nodes x and y of the graph.

A graph is a valid tree when all the nodes are connected and there is
no cycle between them.

Constraints:
- 1 <= n <= 1000
- 0 <= edges.length <= 2000
- edges[i].length = 2
- 0 <= x, y < n
- x != y
- There are no repeated edges.

Example 1:
Input: n = 5, edges = [[0,1], [0,2], [0,3], [1,4]]
Output: True
Explanation: All nodes are connected with no cycles.

Example 2:
Input: n = 5, edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: False
Explanation: There is a cycle: 1 -> 2 -> 3 -> 1
"""

"""
n = 7
edges = [1,2], [1,3], [2,4], [2,5],[3,6],[3,7]

visited = (1 2 3 4 5 6 7)

"""

"""
(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])   

"""

"""
Input: n = 5, edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]

adj
    0 -> [1]
    1 -> [0,2,3,4]
    2 -> [1,3]
    3 -> [1,2]
    4 -> [1]

visited = (0,1)
q = 
m = [0,1]
"""

from collections import deque
def solution(n: int, edges: list[list[int]]) -> bool:
    # time = O(E + V)
    # space = O(V + E)

    if n == 1:
        return True

    if len(edges) < n-1 : 
        return False

    adj = {}
    visited = set()

    for i in range(n): # V
        adj[i] = []

    for e in edges: # E
        adj[e[0]].append(e[1])
        adj[e[1]].append(e[0])

    
    q = deque()
    q.append([-1,0])
    visited.add(0)

    while len(q) > 0 : # E
        m = q.pop()
        for nb in adj[m[1]]:
            if nb not in visited:
                q.append([m[1],nb])
                visited.add(nb)
            else:
                if nb != m[0]:
                    return False

    return True





TEST_CASES = [
    # (input_args, expected_output)
    ((5, [[0, 1], [0, 2], [0, 3], [1, 4]]), True),
    ((5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]), False),
    # Single node, no edges - valid tree
    ((1, []), True),
    # Two nodes, one edge - valid tree
    ((2, [[0, 1]]), True),
    # Two nodes, no edges - not connected
    ((2, []), False),
    # Disconnected components
    ((4, [[0, 1], [2, 3]]), False),
    # Linear tree
    ((4, [[0, 1], [1, 2], [2, 3]]), True),
]
