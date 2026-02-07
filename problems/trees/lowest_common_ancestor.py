"""
Problem: Lowest Common Ancestor of a Binary Tree
Difficulty: Medium
Time Limit: 30 minutes

Description:
Given the root node of a binary tree with n nodes, find the lowest common
ancestor (LCA) of two of its nodes, p and q.

The lowest common ancestor is defined as the lowest node in the binary tree
that has both p and q as descendants. A node can be a descendant of itself.

Example 1:
        3
       / \
      5   1
     / \ / \
    6  2 0  8
      / \
     7   4

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2 (same tree):
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a
             descendant of itself.

Example 3:
Input: root = [1,2], p = 1, q = 2
Output: 1

Constraints:
- 2 <= n <= 500
- All Node.data are unique
- p != q
- p and q exist in the tree
"""


class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.data})"


def solution(root, p, q):
    """
    Find the lowest common ancestor of nodes p and q in the binary tree.

    Args:
        root: Root TreeNode of the binary tree
        p: TreeNode to find
        q: TreeNode to find

    Returns:
        TreeNode that is the lowest common ancestor of p and q
    """

    lca = None

    def rec(node,p,q):
        nonlocal lca
        if not node:
            return False
        
        mid, left, right = False, False, False
        if p == node or q == node:
            mid = True
        
        left = rec(node.left, p, q)
        if not lca:
            right = rec(node.right, p, q)

        if mid + left + right >= 2:
            lca = node

        return mid or left or right
        
    rec(root,p,q)

    return lca



# ============== Test Infrastructure (Do Not Modify) ==============

def build_tree(values):
    """Build a binary tree from level-order list. None means no node."""
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def find_node(root, val):
    """Find a node with given value in the tree."""
    if root is None:
        return None
    if root.data == val:
        return root
    left = find_node(root.left, val)
    if left:
        return left
    return find_node(root.right, val)


def solution_wrapper(tree_values, p_val, q_val, expected_val):
    """Wrapper that builds the tree, finds p/q nodes, calls solution, and checks result."""
    root = build_tree(tree_values)
    p = find_node(root, p_val)
    q = find_node(root, q_val)
    result = solution(root, p, q)
    if result is None:
        return None
    return result.data


TEST_CASES = [
    # ((tree_values, p_val, q_val, expected_val), expected_output)
    (([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1, 3), 3),
    (([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4, 5), 5),
    (([1, 2], 1, 2, 1), 1),
    (([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 6, 4, 5), 5),
    (([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 0, 8, 1), 1),
    (([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 7, 8, 3), 3),
]
