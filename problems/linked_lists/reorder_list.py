"""
Problem: Reorder List
Difficulty: Medium
Time Limit: 30 min

Given the head of a singly linked list, reorder the list as if it were folded
on itself.

Original order:
L0 → L1 → L2 → ... → Ln-2 → Ln-1 → Ln

Reordered:
L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...

You don't need to modify the values in the list's nodes; only the links
between nodes need to be changed.

Example 1:
Input: head = [1, 2, 3, 4]
Output: [1, 4, 2, 3]
Explanation: Fold the list - first connects to last, second to second-last, etc.

Example 2:
Input: head = [1, 2, 3, 4, 5]
Output: [1, 5, 2, 4, 3]
Explanation: Middle element (3) stays in place at the end.

Example 3:
Input: head = [1]
Output: [1]
Explanation: Single node - nothing to reorder.

Constraints:
- The number of nodes in the list is in the range [1, 500]
- -5000 <= Node.val <= 5000
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
"""
    head -> 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    output -> 1, 10, 2, 9, 3, 8, 4, 7, 5, 6

    -- find the middle.. break list into 2
    -- rever the second list
    -- zip them together
"""
def solution(head: ListNode | None) -> None:
    """
    Reorder the list in-place. Do not return anything.

    TODO(human): Implement your solution

    Think about:
    - How can you access the "end" nodes of a singly linked list?
    - What sub-problems does this break down into?

    head -> 1, 2, 3, 4, 5, 6, 7, 8, 9

    slow -> 5
    fast -> 9

    head2 -> 6

    None <- 5 <- 6 <- 7 <- 8 <- 9
    prev -> 9
    curr -> 10
    nxt -> None

    head -> 1, 2, 3, 4
    head2 -> 1 -> 9 -> 2 -> 8 -> 3 -> 7 -> 4  -> 6 -> None, 5

    
    p -> None
    q -> 5
    np -> None
    nq -> 5


    head -> 1 -> None, head2 -> 2, 3

    slow -> 2
    fast -> 3
    prev -> 1
    """

    if head is None or head.next is None:
        return head
    
    slow, fast = head, head
    prev = None

    while fast is not None and fast.next != None:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    head2 = slow
    prev.next = None   
    

    prev, curr, nxt = None, head2, head2.next

    while nxt is not None:
        curr.next = prev
        prev = curr
        curr = nxt
        nxt = nxt.next
        
    curr.next = prev

    head2 = curr

    p = head
    q = head2
    pq = None

    while q is not None and p is not None:
        np = p.next
        nq = q.next
        q.next = p.next
        p.next = q
        pq = q
        p = np
        q = nq

    if p is None and q is not None:
        pq.next = q
            
    return head


# ----- Test Case Wrapper (DO NOT MODIFY) -----

_original_solution = solution


def _test_wrapper(arr: list) -> list:
    """Wrapper to convert test inputs/outputs for the runner."""
    head = list_to_linked(arr)
    _original_solution(head)
    return linked_to_list(head)


# Override solution for test runner
solution = _test_wrapper


TEST_CASES = [
    # Single node - nothing to reorder
    (([1],), [1]),

    # Two nodes - already in correct order
    (([1, 2],), [1, 2]),

    # Three nodes: 1->2->3 becomes 1->3->2
    (([1, 2, 3],), [1, 3, 2]),

    # Four nodes: 1->2->3->4 becomes 1->4->2->3
    (([1, 2, 3, 4],), [1, 4, 2, 3]),

    # Five nodes: 1->2->3->4->5 becomes 1->5->2->4->3
    (([1, 2, 3, 4, 5],), [1, 5, 2, 4, 3]),

    # Six nodes: even length
    (([1, 2, 3, 4, 5, 6],), [1, 6, 2, 5, 3, 4]),

    # Seven nodes: odd length
    (([1, 2, 3, 4, 5, 6, 7],), [1, 7, 2, 6, 3, 5, 4]),

    # With negative values
    (([-5, 0, 5, 10],), [-5, 10, 0, 5]),

    # Longer list
    (([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],), [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]),
]
