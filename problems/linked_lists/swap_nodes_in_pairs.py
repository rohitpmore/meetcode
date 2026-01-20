"""
Problem: Swap Nodes in Pairs
Difficulty: Medium
Time Limit: 30 min

Given a singly linked list, swap every two adjacent nodes and return the head
of the modified list.

Important: Solve this problem without modifying the values in the list's nodes.
Only the node links themselves can be changed.

Example 1:
Input: head = [1, 2, 3, 4]
Output: [2, 1, 4, 3]
Explanation:
  Before: 1 -> 2 -> 3 -> 4
  After:  2 -> 1 -> 4 -> 3
  (1,2) swapped, (3,4) swapped

Example 2:
Input: head = []
Output: []
Explanation: Empty list - nothing to swap.

Example 3:
Input: head = [1]
Output: [1]
Explanation: Single node - no pair to swap.

Example 4:
Input: head = [1, 2, 3]
Output: [2, 1, 3]
Explanation: Only first pair swapped, 3 has no partner.

Constraints:
- The number of nodes in the list is in the range [0, 100]
- 0 <= Node.val <= 100
"""

# ----- Linked List Infrastructure (DO NOT MODIFY) -----

class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val})"


def list_to_linked(arr: list) -> ListNode | None:
    """Convert a Python list to a linked list."""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_to_list(head: ListNode | None) -> list:
    """Convert a linked list back to a Python list."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


# ----- Your Solution Below -----

def solution(head: ListNode | None) -> ListNode | None:
    """
    Swap every two adjacent nodes and return the modified list head.

    TODO(human): Implement your solution

    Think about:
    - What pointers do you need to track to swap two nodes?
    - How do you connect the swapped pair to the previous part of the list?
    - What happens when there's an odd number of nodes?

    head -> 1,2, 3, 4, 5,6,7
    output -> 2, 1,4, 3, 6, 5, 7

    dummy ->  2 -> 1 -> 4 -> 3 -> 6 -> 5 -> 7 -> None

    prev -> 5
    p -> 7
    np ->   
    q -> 
    """
    if head is None or head.next is None:
        return head
    
    dummy = ListNode(0, head)

    p = head
    prev = dummy

    while p is not None and p.next is not None:
        q = p.next
        np = q.next
        q.next = p 
        p.next = np
        prev.next = q
        prev = p
        p = np

    return dummy.next

# ----- Test Case Wrapper (DO NOT MODIFY) -----

_original_solution = solution


def _test_wrapper(arr: list) -> list:
    """Wrapper to convert test inputs/outputs for the runner."""
    head = list_to_linked(arr)
    result = _original_solution(head)
    return linked_to_list(result)


# Override solution for test runner
solution = _test_wrapper


TEST_CASES = [
    # Empty list
    (([], ), []),

    # Single node - nothing to swap
    (([1], ), [1]),

    # Two nodes - one swap
    (([1, 2], ), [2, 1]),

    # Three nodes - first pair swaps, third stays
    (([1, 2, 3], ), [2, 1, 3]),

    # Four nodes - two complete swaps
    (([1, 2, 3, 4], ), [2, 1, 4, 3]),

    # Five nodes - two swaps, fifth stays
    (([1, 2, 3, 4, 5], ), [2, 1, 4, 3, 5]),

    # Six nodes - three complete swaps
    (([1, 2, 3, 4, 5, 6], ), [2, 1, 4, 3, 6, 5]),

    # Longer list with even length
    (([1, 2, 3, 4, 5, 6, 7, 8], ), [2, 1, 4, 3, 6, 5, 8, 7]),

    # Longer list with odd length
    (([1, 2, 3, 4, 5, 6, 7], ), [2, 1, 4, 3, 6, 5, 7]),

    # Same values
    (([5, 5, 5, 5], ), [5, 5, 5, 5]),
]
