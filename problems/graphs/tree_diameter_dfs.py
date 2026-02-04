"""
Problem: Tree Diameter (Single DFS approach)
Difficulty: Medium

Given an undirected tree with n nodes labeled from 0 to n-1, represented by
a 2D array edges where edges.length == n-1. Each edges[i] = [ai, bi] denotes
an undirected edge between nodes ai and bi.

Return the diameter of the tree.

The diameter of a tree is the number of edges in the longest path between
any two nodes.

Approach: Single DFS traversal tracking the two longest paths from each node.

Constraints:
- n == edges.length + 1
- edges[i].length = 2
- 1 <= n <= 10^3
- 0 <= ai, bi < n
- ai != bi
"""


def solution(edges: list[list[int]]) -> int:
    if len(edges) == 0 :
        return 0

    adj = {}

    for i in range(len(edges)+1):
        adj[i] = []
    
    for e in edges:
        adj[e[0]].append(e[1])
        adj[e[1]].append(e[0])
    


    def rec(node,parent):
        nonlocal diameter
        l, sl = 0, 0
        for nb in adj[node]:
            if nb != parent:
                d = rec(nb, node)
                if d > l : 
                    l = d
                elif d > sl:
                    sl = d
        
        diameter = max(diameter, l + sl)
        return l + 1
            
    diameter = 0
    rec(0,-1)

    return diameter


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
