"""
Problem: Reverse Linked List II
Difficulty: Medium
Time Limit: 30 min

Given a singly linked list and two positions, left and right, reverse the nodes
of the list from position left to position right. Return the modified list.

Positions are 1-indexed (the first node is at position 1).

Example 1:
Input: head = [1, 2, 3, 4, 5], left = 2, right = 4
Output: [1, 4, 3, 2, 5]
Explanation:
  Before: 1 -> 2 -> 3 -> 4 -> 5
  After:  1 -> 4 -> 3 -> 2 -> 5
  Nodes at positions 2-4 are reversed.

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]
Explanation: Single node, nothing to reverse.

Example 3:
Input: head = [1, 2, 3, 4, 5], left = 1, right = 5
Output: [5, 4, 3, 2, 1]
Explanation: Entire list is reversed.

Example 4:
Input: head = [1, 2, 3], left = 1, right = 2
Output: [2, 1, 3]
Explanation: Only the first two nodes are reversed.

Constraints:
- 1 <= n <= 500 (n is the number of nodes)
- -5000 <= Node.val <= 5000
- 1 <= left <= right <= n
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

def solution(head: ListNode | None, left: int, right: int) -> ListNode | None:
    """
    Reverse the nodes from position left to position right (1-indexed).

    TODO(human): Implement your solution

    Think about:
    - How do you reach the node just before position 'left'?
    - How do you reverse a sublist of a linked list?
    - How do you reconnect the reversed portion back to the rest?
    - What if left = 1 (reversing from the head)?

    1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> None
    op ->     1 -> 5 -> 4 ->3 -> 2 -> 6 -> 7 -> None
    
    left -> 2
    right -> 5
    dummy -> 1 -> 5 -> 4 -> 3 -> 2 -> 6 -> 7 -> None
    lp -> 2
    rp -> 5
    prev -> 1 

    p -> 4
    c -> 5
    n -> 6
    """
    if head is None or head.next is None:
        return head

    if left == right:
        return head
    
    """ 
    dummy -> 1->2
    left = 1
    right = 2
    lp = 1
    rp = 2
    prev = dummy

    dummy <- 1 <- 2 -> None
    p = 1
    c = 2
    n = None

    """
    dummy = ListNode(0, head)
    lp, rp = dummy, dummy
    before = None

    for i in range(left):
        i += 1
        before = lp
        lp = lp.next

    for i in range(right):
        i += 1
        rp = rp.next

    p = before
    c = lp
    n = lp.next
    after = rp.next

    while n is not None and c != after:
        c.next = p
        p = c
        c = n
        n = n.next
    if c != after :
        c.next = p
    lp.next = after
    before.next = rp

    return dummy.next


# ----- Test Case Wrapper (DO NOT MODIFY) -----

_original_solution = solution


def _test_wrapper(arr: list, left: int, right: int) -> list:
    """Wrapper to convert test inputs/outputs for the runner."""
    head = list_to_linked(arr)
    result = _original_solution(head, left, right)
    return linked_to_list(result)


# Override solution for test runner
solution = _test_wrapper


TEST_CASES = [
    # Single node - nothing to reverse
    (([5], 1, 1), [5]),

    # Two nodes - swap them
    (([1, 2], 1, 2), [2, 1]),

    # Two nodes - reverse nothing (left == right)
    (([1, 2], 2, 2), [1, 2]),

    # Reverse middle section
    (([1, 2, 3, 4, 5], 2, 4), [1, 4, 3, 2, 5]),

    # Reverse from head
    (([1, 2, 3, 4, 5], 1, 3), [3, 2, 1, 4, 5]),

    # Reverse to tail
    (([1, 2, 3, 4, 5], 3, 5), [1, 2, 5, 4, 3]),

    # Reverse entire list
    (([1, 2, 3, 4, 5], 1, 5), [5, 4, 3, 2, 1]),

    # Reverse single node in middle
    (([1, 2, 3, 4, 5], 3, 3), [1, 2, 3, 4, 5]),

    # Three nodes - reverse all
    (([1, 2, 3], 1, 3), [3, 2, 1]),

    # Longer list - reverse middle portion
    (([1, 2, 3, 4, 5, 6, 7, 8], 3, 6), [1, 2, 6, 5, 4, 3, 7, 8]),

    # With negative values
    (([-5, 0, 5, 10, 15], 2, 4), [-5, 10, 5, 0, 15]),
]
