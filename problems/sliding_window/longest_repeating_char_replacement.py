"""
Problem: Longest Repeating Character Replacement
Difficulty: Medium
Time Limit: 30 minutes

Description:
Given a string, s, and an integer, k, find the length of the longest substring
in s, where all characters are identical, after replacing at most k characters
with any other uppercase English character.

Constraints:
- 1 <= s.length <= 10^3
- s consists of only uppercase English characters.
- 0 <= k <= s.length

Examples:

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace both 'A's with 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' to get "AABBBBA".
The substring "BBBB" has length 4.

Example 3:
Input: s = "ABCDE", k = 1
Output: 2
Explanation: Replace any one character to get two adjacent identical chars.
"""


def solution(s: str, k: int) -> int:

    """ 
    s -> ABBB, k-> 2
    L -> 4

    ws -> 0
    we -> 3
    max_count = 3
    count{'A':1, 'B':3}




    """
    if len(s) == 1:
        return 1
    
    ws, we = 0, 0 
    lrc = 0
    L = len(s)
    count = {}
    max_count = 0

    for we in range(L):
        count[s[we]] = count.get(s[we],0) + 1
        max_count = max(max_count, count[s[we]])

        while we - ws + 1 - max_count > k:
            count[s[ws]] -= 1
            ws += 1
    
        lrc = max(lrc, we - ws + 1)
    return lrc



TEST_CASES = [
    (("ABAB", 2), 4),
    (("AABABBA", 1), 4),
    (("ABCDE", 1), 2),
    (("AAAA", 2), 4),
    (("ABCD", 0), 1),
    (("AABCCBB", 2), 5),
    (("ABBCB", 1), 4),
    (("ABBB", 2), 4),
]
