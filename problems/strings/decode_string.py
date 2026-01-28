"""
Problem: Decode String
Difficulty: Medium

Given an encoded string, return its decoded version. The encoding rule follows
the pattern: k[encoded_string], where the encoded_string inside the square
brackets is repeated exactly k times.

Rules:
- k is guaranteed to be a positive integer
- Input string is always valid (balanced brackets, well-formed)
- Original data contains no digits (digits only for repeat count)
- Patterns can be nested: k[string k2[nested]]

Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Explanation: "a" repeated 3 times + "bc" repeated 2 times

Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"
Explanation: Inner first: 2[c] = "cc", then 3[acc] = "accaccacc"

Example 3:
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Explanation: "abc" × 2 + "cd" × 3 + "ef"

Example 4:
Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"
Explanation: "abc" + "cd" × 3 + "xyz"

Example 5:
Input: s = "10[a]"
Output: "aaaaaaaaaa"
Explanation: Multi-digit number: "a" repeated 10 times

Constraints:
- 1 <= s.length <= 30
- 1 <= k <= 100
- s consists of lowercase English letters, digits, and square brackets
"""

"""
2[aj]3[bax]
ajajbaxbaxbax

3[a2[c]]
3[acc]
accaccacc
"""

from collections import deque

def solution(s: str) -> str:
    """
    Decode the encoded string and return the result.
    """
    st = deque()
    


TEST_CASES = [
    (("3[a]2[bc]",), "aaabcbc"),
    (("3[a2[c]]",), "accaccacc"),
    (("2[abc]3[cd]ef",), "abcabccdcdcdef"),
    (("abc3[cd]xyz",), "abccdcdcdxyz"),
    (("10[a]",), "aaaaaaaaaa"),
    (("a",), "a"),  # Single character, no encoding
    (("abc",), "abc"),  # No encoding at all
    (("2[2[b]]",), "bbbb"),  # Nested same depth
    (("3[a]2[b]4[c]",), "aaabbcccc"),  # Multiple sequential
    (("2[a2[b3[c]]]",), "abcccbcccabcccbccc"),  # Deep nesting
]
