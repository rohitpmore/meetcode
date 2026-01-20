"""
Problem: Remove Nth Node From End of List
Difficulty: Medium
Source: LeetCode #19

Given the head of a singly linked list and an integer n, remove the nth node
from the end of the list and return the head of the modified list.

Example 1:
Input: head = [1, 2, 3, 4, 5], n = 2
Output: [1, 2, 3, 5]
Explanation: The 2nd node from end is 4, so we remove it.

Example 2:
Input: head = [1], n = 1
Output: []
Explanation: The only node is removed.

Example 3:
Input: head = [1, 2], n = 1
Output: [1]
Explanation: The 1st node from end is 2, so we remove it.

Constraints:
- The number of nodes in the list is k
- 1 <= k <= 1000
- -1000 <= Node.val <= 1000
- 1 <= n <= k
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

def solution(head: ListNode | None, n: int) -> ListNode | None:
    # TODO(human): Refactor using a dummy node
    # Hint: dummy = ListNode(0, head), then work from dummy
    # Your solution should need only ~8-10 lines with minimal if statements

    dummy = ListNode(0, head)
    p1, p2 = dummy, dummy

    i = 0

    while i < n and p1.next != None :
        p1 = p1.next
        i += 1

    while p1.next != None :
        p1 = p1.next
        p2 = p2.next

    if p2.next != None :
        p2.next = p2.next.next

    return dummy.next

# d -> 1 -> 2 -> END
# n = 2

# p1 = 2
# p2 = d
# ----- Test Case Wrapper (DO NOT MODIFY) -----

# Store the original solution before overriding
_original_solution = solution


def _test_wrapper(arr: list, n: int) -> list:
    """Wrapper to convert test inputs/outputs for the runner."""
    head = list_to_linked(arr)
    result = _original_solution(head, n)
    return linked_to_list(result)


# Override solution for test runner
solution = _test_wrapper


TEST_CASES = [
    # Basic cases from examples
    (([1, 2, 3, 4, 5], 2), [1, 2, 3, 5]),       # Remove 4 (2nd from end)
    (([1], 1), []),                              # Remove only node
    (([1, 2], 1), [1]),                          # Remove last node

    # Remove first node (nth from end where n = length)
    (([1, 2], 2), [2]),                          # Remove first node
    (([1, 2, 3], 3), [2, 3]),                    # Remove head

    # Remove from middle
    (([1, 2, 3, 4, 5], 3), [1, 2, 4, 5]),       # Remove 3 (3rd from end)
    (([1, 2, 3, 4, 5], 4), [1, 3, 4, 5]),       # Remove 2 (4th from end)

    # Remove last node
    (([1, 2, 3, 4, 5], 1), [1, 2, 3, 4]),       # Remove 5 (1st from end)

    # Longer list
    (([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5), [1, 2, 3, 4, 5, 7, 8, 9, 10]),

    # Two elements
    (([1, 2], 1), [1]),                          # Remove last
    (([1, 2], 2), [2]),                          # Remove first
]
