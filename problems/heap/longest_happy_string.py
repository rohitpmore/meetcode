"""
Problem: Longest Happy String
Difficulty: Medium

A string is considered happy if it meets the following conditions:
- It comprises only the characters 'a', 'b', and 'c'.
- It does not contain the substrings "aaa", "bbb", or "ccc".
- The total occurrences of:
  - The character 'a' does not exceed a.
  - The character 'b' does not exceed b.
  - The character 'c' does not exceed c.

You are given three integers, a, b, and c, representing the maximum allowable
occurrences of 'a', 'b', and 'c', respectively. Your task is to return the
longest possible happy string.

If there are multiple valid longest happy strings, return any one of them.
If no such string can be formed, return an empty string "".

Note: A substring is a contiguous sequence of characters within a string.

Constraints:
- 0 <= a, b, c <= 100
- a + b + c > 0

Example 1:
Input: a = 1, b = 1, c = 7
Output: "ccaccbcc" (or "ccbccacc", etc.)
Explanation: "ccbccacc" is also valid. Length = 8.

Example 2:
Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: Only 'a' and 'b' available. Max length = 5.

Example 3:
Input: a = 2, b = 2, c = 1
Output: "aabbc" (or "abbca", etc.)
Explanation: Multiple valid answers exist. Length = 5.
"""

import heapq


def solution(a: int, b: int, c: int) -> str:
    """
    Generate the longest happy string given counts of 'a', 'b', and 'c'.

    Args:
        a: Maximum occurrences of 'a'
        b: Maximum occurrences of 'b'
        c: Maximum occurrences of 'c'

    Returns:
        str: The longest happy string possible
    """

    """
    a = 1
    b = 1 
    c = 7

    bow =  (-1,c)
    hs = ['c','c','a','c','c','b','c','c']
    """
    bow = []
    if a > 0:
        bow.append([-a,'a'])

    if b > 0:
        bow.append([-b,'b'])

    if c > 0:
        bow.append([-c,'c'])

    heapq.heapify(bow)
    hs = []

    while len(bow) > 0:
        ch1 = heapq.heappop(bow)
        prev1 = hs[-1] if len(hs) >= 1 else None
        prev2 = hs[-2] if len(hs) >= 2 else None
        if ch1[1] == prev1 and ch1[1] == prev2:
            if len(bow) == 0:
                break
            ch2 = heapq.heappop(bow)
            hs.append(ch2[1])
            if ch2[0]+ 1 != 0 :
                heapq.heappush(bow,[ch2[0]+ 1, ch2[1]])
            heapq.heappush(bow,[ch1[0], ch1[1]])
        else:
            hs.append(ch1[1])
            if ch1[0]+ 1 != 0:
                heapq.heappush(bow, [ch1[0]+ 1, ch1[1]])


    return len(hs)



    

def validate_happy_string(result: str, a: int, b: int, c: int) -> bool:
    """Validates that a string is a valid happy string."""
    if not result:
        return True
    # Check no "aaa", "bbb", "ccc"
    if "aaa" in result or "bbb" in result or "ccc" in result:
        return False
    # Check character counts don't exceed limits
    if result.count('a') > a or result.count('b') > b or result.count('c') > c:
        return False
    # Check only valid characters
    if not all(ch in 'abc' for ch in result):
        return False
    return True


# Expected lengths for each test case (since multiple valid answers exist)
EXPECTED_LENGTHS = {
    (1, 1, 7): 8,   # e.g., "ccaccbcc"
    (7, 1, 0): 5,   # e.g., "aabaa"
    (2, 2, 1): 5,   # e.g., "aabbc"
    (0, 0, 1): 1,   # "c"
    (1, 0, 0): 1,   # "a"
    (0, 8, 11): 19, # Mix of b and c
    (3, 3, 3): 9,   # Equal counts - "abcabcabc"
}

TEST_CASES = [
    ((1, 1, 7), 8),      # c dominates
    ((7, 1, 0), 5),      # a dominates, no c
    ((2, 2, 1), 5),      # balanced
    ((0, 0, 1), 1),      # only c
    ((1, 0, 0), 1),      # only a
    ((0, 8, 11), 19),    # b and c only
    ((3, 3, 3), 9),      # perfectly balanced
]
