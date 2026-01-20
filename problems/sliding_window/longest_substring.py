"""
Problem: Longest Substring Without Repeating Characters
Difficulty: Medium
Time Limit: 30 minutes

Description:
Given a string, input_str, return the length of the longest substring
without repeating characters.

Constraints:
- 1 <= input_str.length <= 10^5
- input_str consists of English letters, digits, and spaces.

Examples:

Example 1:
Input: input_str = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with length 3.

Example 2:
Input: input_str = "bbbbb"
Output: 1
Explanation: The answer is "b", with length 1.

Example 3:
Input: input_str = "pwwkew"
Output: 3
Explanation: The answer is "wke", with length 3.
Note: "pwke" is a subsequence, not a substring.
"""


def solution(input_str: str) -> int:
    # TODO(human): Implement your solution

    """
    abcdefbs -> 6
        ws -> 2
        we -> 7
        curLen -> 2
        longest -> 6

    dvdf
        L -> 4
        ws -> 1
        we -> 2
        longest -> 2
        curLen -> 1

    aabc efha -> 7
    1234563 -> 6
    a -> 1
    ab -> 2
    aa -> 1
    """
    L = len(input_str)
    if L == 1:
        return 1

    ws, we = 0,0
    longest = 0
    visited = {}

    while we < L and ws < L:
        visited[input_str[we]] = we
        we += 1
        curLen = we - ws
        
        while we < L and input_str[we] not in visited:
            visited[input_str[we]] = we
            we += 1
            curLen += 1
        longest = max(longest, curLen)
        
        if we == L:
            return longest
        
        if input_str[we] in visited:
            ws = max(ws,visited.get(input_str[we]) + 1)

    return longest


TEST_CASES = [
    (("abcabcbb",), 3),
    (("abcdbea",), 5),
    (("bbbbb",), 1),
    (("pwwkew",), 3),
    ((" ",), 1),
    (("au",), 2),
    (("dvdf",), 3),
    (("abcdef",), 6),
    (("aab",), 2),
]
