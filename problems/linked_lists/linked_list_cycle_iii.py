"""
Problem: Linked List Cycle III
Difficulty: Medium

Given the head of a linked list, determine the length of the cycle present
in the linked list. If there is no cycle, return 0.

A cycle exists in a linked list if there is some node in the list that can
be reached again by continuously following the next pointer.

Example 1:
Input: head = [3, 2, 0, -4], cycle_pos = 1
       3 -> 2 -> 0 -> -4
            ^         |
            |_________|
Output: 3
Explanation: The cycle has nodes [2, 0, -4], so length is 3.

Example 2:
Input: head = [1, 2], cycle_pos = 0
       1 -> 2
       ^    |
       |____|
Output: 2
Explanation: The cycle includes both nodes [1, 2], length is 2.

Example 3:
Input: head = [1], cycle_pos = -1
       1 -> None
Output: 0
Explanation: No cycle exists.

Constraints:
- The number of nodes in the list is in the range [0, 10^4]
- -10^5 <= Node.val <= 10^5
- cycle_pos is -1 (no cycle) or a valid index in the list
"""

# ----- Linked List Infrastructure (DO NOT MODIFY) -----


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val})"


def create_cyclic_list(arr: list, cycle_pos: int) -> ListNode | None:
    """
    Create a linked list from array, with optional cycle.

    Args:
        arr: List of node values
        cycle_pos: Index where tail connects to (-1 for no cycle)

    Returns:
        Head of the (possibly cyclic) linked list
    """
    if not arr:
        return None

    # Create all nodes
    nodes = [ListNode(val) for val in arr]

    # Link nodes
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    # Create cycle if specified
    if cycle_pos >= 0 and cycle_pos < len(nodes):
        nodes[-1].next = nodes[cycle_pos]

    return nodes[0]


# ----- Your Solution Below -----
"""
Example 1
list -> [], length = 0
list -> [1], length = 0

list -> [0 1 2 3 4 1]
    slow -> 0 1 2 3 4 
    fast -> 0 2 4 2 4 1 2 4
    length -> 4

"""

def solution(head: ListNode | None) -> int:
    """
    Return the length of the cycle in the linked list.
    Return 0 if no cycle exists.
    """
    # TODO(human): Implement your solution
    if head is None or head.next is None:
        return 0
    
    slow, fast = head, head
    isCycle = False
    length = 0

    while slow is not None and fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if isCycle:
            length += 1

        if slow == fast:
            if isCycle:
                break
            if not isCycle:
                isCycle = True

        
    return length


# ----- Test Case Wrapper (DO NOT MODIFY) -----

_original_solution = solution


def _test_wrapper(arr: list, cycle_pos: int) -> int:
    """Wrapper to convert test inputs for the runner."""
    head = create_cyclic_list(arr, cycle_pos)
    return _original_solution(head)


# Override solution for test runner
solution = _test_wrapper


TEST_CASES = [
    # (([node_values], cycle_position), expected_cycle_length)
    # cycle_position = -1 means no cycle

    # No cycle cases
    (([1], -1), 0),                    # Single node, no cycle
    (([1, 2], -1), 0),                 # Two nodes, no cycle
    (([1, 2, 3, 4, 5], -1), 0),        # Multiple nodes, no cycle
    (([], -1), 0),                     # Empty list

    # Cycle cases
    (([3, 2, 0, -4], 1), 3),           # Cycle of length 3 (2->0->-4->2)
    (([1, 2], 0), 2),                  # Cycle of length 2 (1->2->1)
    (([1], 0), 1),                     # Single node cycle (1->1)
    (([1, 2, 3, 4], 0), 4),            # Full list is cycle
    (([1, 2, 3, 4], 2), 2),            # Cycle of length 2 (3->4->3)
    (([1, 2, 3, 4, 5], 3), 2),         # Cycle at end (4->5->4)

    # Edge cases
    (([1, 2, 3, 4, 5, 6], 1), 5),      # Long cycle
    (([1, 2, 3, 4, 5, 6, 7, 8], 4), 4),  # Cycle in second half
]
