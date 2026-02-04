"""
Problem: Tree Diameter
Difficulty: Medium

Given an undirected tree with n nodes labeled from 0 to n-1, represented by
a 2D array edges where edges.length == n-1. Each edges[i] = [ai, bi] denotes
an undirected edge between nodes ai and bi.

Return the diameter of the tree.

The diameter of a tree is the number of edges in the longest path between
any two nodes.

Constraints:
- n == edges.length + 1
- edges[i].length = 2
- 1 <= n <= 10^3
- 0 <= ai, bi < n
- ai != bi

Example 1:
Input: n = 4, edges = [[0,1], [1,2], [2,3]]
Output: 3
Explanation: Longest path is 0 -> 1 -> 2 -> 3 (3 edges)

Example 2:
Input: n = 5, edges = [[0,1], [0,2], [0,3], [0,4]]
Output: 2
Explanation: Longest path is between any two leaf nodes through 0 (2 edges)
"""

"""
edges = [[0,1], [0,2], [0,3], [0,4]]

adj
    0 -> [1,2,3,4]
    1 -> [0]
    2 -> [0]
    3 -> [0]
    4 -> [0]

visited = (1,0,2,3,4)
q = [2,2] [3,2] [4,2]
node = 0
dist = 1
maxd = 1
fnode = 0
"""

from collections import deque
def solution(edges: list[list[int]]) -> int:

    # time = O(V + E)
    # space = O(V + E)
    if len(edges) == 0 :
        return 0

    visited = set()
    q = deque()
    adj = {}

    for i in range(len(edges) + 1): # V
        adj[i] = []

    for e in edges: # E
        adj[e[0]].append(e[1])
        adj[e[1]].append(e[0])
    
    q.append([0,0])
    visited.add(0)
    maxd = -1
    fnode = -1

    while len(q) > 0 : # V
        [node,dist] = q.pop()
        if dist > maxd:
            maxd = dist
            fnode = node

        for nb in adj[node]:
            if nb not in visited:
                q.append([nb,dist+1])
                visited.add(nb)

    q = deque()
    visited = set()
    q.append([fnode,0])
    visited.add(fnode)
    maxd = -1

    while len(q) > 0 :
        [node,dist] = q.pop()
        if dist > maxd:
            maxd = dist

        for nb in adj[node]:
            if nb not in visited:
                q.append([nb,dist+1])
                visited.add(nb)

    return maxd


TEST_CASES = [
    # (input_args, expected_output)
    # Linear tree: 0 - 1 - 2 - 3
    (([[0, 1], [1, 2], [2, 3]],), 3),
    # Star tree: all connected to center
    (([[0, 1], [0, 2], [0, 3], [0, 4]],), 2),
    # Single node
    (([],), 0),
    # Two nodes
    (([[0, 1]],), 1),
    # Balanced binary tree shape
    #       0
    #      / \
    #     1   2
    #    / \
    #   3   4
    (([[0, 1], [0, 2], [1, 3], [1, 4]],), 3),
]
