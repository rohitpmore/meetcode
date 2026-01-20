"""
Problem: Circular Array Loop
Difficulty: Medium

There is a circular list of non-zero integers called nums. Each number tells you
how many steps to move forward or backward from your current position:
- If nums[i] is positive, move nums[i] steps forward
- If nums[i] is negative, move nums[i] steps backward

As the list is circular:
- Moving forward from the last element takes you back to the first element
- Moving backward from the first element takes you to the last element

A valid cycle in this list means:
1. You keep moving and end up repeating a sequence of indexes
2. All numbers in the cycle have the SAME SIGN (all positive or all negative)
3. The cycle length is GREATER THAN 1 (involves at least two indexes)

Return True if such a cycle exists, False otherwise.

Constraints:
- 1 <= nums.length <= 10^3
- -5000 <= nums[i] <= 5000
- nums[i] != 0

Example 1:
Input: nums = [2, -1, 1, 2, 2]
Output: True
Explanation: Cycle exists: index 0 -> 2 -> 3 -> 0 (all positive, length 3)

Example 2:
Input: nums = [-1, -2, -3, -4, -5]
Output: False
Explanation: No valid cycle with same-sign and length > 1

Example 3:
Input: nums = [1, -1, 5, 1, 4]
Output: True
Explanation: Cycle exists: index 0 -> 1 -> 0... wait, signs differ!
             But index 3 -> 4 -> 3 works (both positive, length 2)

Example 4:
Input: nums = [2, -1, 1, -2, -2]
Output: False
Explanation: No valid cycle - signs change or self-loops only
"""

"""
Time Complexity = O(n)
Space Complexity = O(n)
"""
    
def solution(nums):
    # TODO(human): Implement your solution
    def get_next(i):
        return (i + nums[i]) % len(nums)
    

    for i in range(len(nums)):
        if nums[i] == 0:
            continue

        path = []
        slow = i
        fast = i

        while True:
            if slow == get_next(slow) or fast == get_next(fast):
                break
            
            path.append(slow)
            
            slow = get_next(slow)
            fast = get_next(get_next(fast))

            if (nums[slow] > 0) != (nums[i] > 0):
                break
            if slow == get_next(slow) or fast == get_next(fast):
                break
            if slow == fast:
                return True
        
        for idx in path:
            nums[idx] = 0

    return False





TEST_CASES = [
    (([2, -1, 1, 2, 2],), True),
    (([-1, -2, -3, -4, -5],), False),
    (([1, -1, 5, 1, 4],), True),
    (([2, -1, 1, -2, -2],), False),
    (([1, 1, 2],), True),           # simple forward cycle
    (([-1, -1, -1],), True),        # simple backward cycle
    (([1],), False),                # single element, can't have length > 1
    (([3, 1, 2],), True),           # all lead to cycle
    (([-2, 1, -1, -2, -2],), False), # mixed signs break cycles
    (([2, 2, 2, 2, 2, 4, 7],), False), # self-loop (index 6 -> 6)
]
