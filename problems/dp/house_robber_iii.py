"""
Problem: House Robber III
Difficulty: Medium
Time Limit: 30 min

A thief has discovered a new neighborhood to target, where the houses can be
represented as nodes in a binary tree. The money in the house is the data of
the respective node.

The thief can enter the neighborhood from a house represented as root of the
binary tree. Each house has only one parent house.

The thief knows that if he robs two houses that are directly connected, the
police will be notified.

Return the maximum amount of money the thief can rob without alerting the police.

Constraints:
- The number of nodes in the tree is in the range [1, 500]
- 0 <= node.data <= 10^4

Example 1:
        3
       / \
      2   3
       \   \
        3   1

Input: root = [3,2,3,null,3,null,1]
Output: 7
Explanation: Rob houses with values 3 + 3 + 1 = 7
(root's left child's right child + root's right child's right child + root)
Actually: Rob 3 (left->right) + 3 (right->right) + ?
Better: Rob root(3) + grandchildren(3+1) = 7

Example 2:
        3
       / \
      4   5
     / \   \
    1   3   1

Input: root = [3,4,5,1,3,null,1]
Output: 9
Explanation: Rob 4 + 5 = 9 (children level)
"""

# Definition for a binary tree node
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree(values: list) -> TreeNode:
    """Helper to build tree from level-order list. None represents null nodes."""
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1

    while queue and i < len(values):
        node = queue.pop(0)

        # Left child
        if i < len(values):
            if values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1

        # Right child
        if i < len(values):
            if values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1

    return root

"""
Example 1:
        3
       / \
      2   3
       \   \
        3   1

Input: root = [3,2,3,null,3,null,1]

rec(3)
    lm = rec(2)
            lm = rec(None)
            <- 0,0
            rm = rec(3)
                    lm = rec(None)
                    <- 0,0
                    rm = rec(None)
                    <- 0,0
            <- 3,0
    <- 2,3
    rm = rec(3)
            lm = rec(None)
            <- 0,0
            rm = rec(1)
                    lm = rec(None)
                    <- 0,0
                    rm = rec(None)
                    <- 0,0
            <- 1,0
    <- 3,1
<- 7,5
"""
def solution(root: TreeNode) -> int:
    """
    Return the maximum money that can be robbed without robbing adjacent houses.
    Adjacent means parent-child relationship in the tree.
    """

    # time = O(n)
    # space = O(log h) --> for recursion stack


    def rec(p:TreeNode):
        if p is None:
            return 0, 0
        
        ly,ln = rec(p.left)
        ry,rn = rec(p.right)

        return p.data + ln + rn , max(ln,ly) + max(rn,ry)

    ry, rn = rec(root)
    return max(ry,rn)



# Wrapper to convert list input to tree for testing
def solution_wrapper(values: list) -> int:
    root = build_tree(values)
    return solution(root)


TEST_CASES = [
    # (input_args, expected_output)
    # Example 1: Rob root + grandchildren = 3 + 3 + 1 = 7
    ([3, 2, 3, None, 3, None, 1], 7),

    # Example 2: Rob children level = 4 + 5 = 9
    ([3, 4, 5, 1, 3, None, 1], 9),

    # Single node
    ([5], 5),

    # Two nodes - pick the larger
    ([1, 2], 2),

    # Three nodes in a line (left skewed): pick root + grandchild
    ([2, 1, None, 3], 5),  # 2 + 3 = 5

    # All same values - alternating levels
    ([1, 1, 1, 1, 1, 1, 1], 5),  # Rob root + 4 grandchildren = 1 + 4 = 5

    # Zero values mixed in
    ([0, 2, 3], 5),  # Rob children = 2 + 3 = 5

    # Larger tree
    ([4, 1, 2, 3], 7),  # Rob root(4) + grandchild(3) = 7
]

# Note: Test runner will call solution_wrapper instead of solution directly
